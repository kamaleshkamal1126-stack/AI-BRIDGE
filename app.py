from flask import Flask, render_template, request, redirect, url_for, session
from database import db, User, Service
import re
from markupsafe import escape


app = Flask(__name__)

# ==================================================
# APP CONFIGURATION
# ==================================================

app.secret_key = "ai-bridge-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ai_bridge.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# ==================================================
# HELPER FUNCTION
# ==================================================

def contains_word(text, word):
    return re.search(
        r"\b" + re.escape(word) + r"\b",
        text
    ) is not None


# ==================================================
# UNDERSTAND USER
# ==================================================

def understand_user(query):

    q = query.lower()

    info = {
        "student": False,
        "department": None,
        "year": None,
        "location": None
    }

    # --------------------------------------------------
    # STUDENT DETECTION
    # --------------------------------------------------

    student_words = [
        "student",
        "students",
        "college",
        "university",
        "studying",
        "study",
        "campus",
        "மாணவர்",
        "மாணவி",
        "கல்லூரி",
        "படிப்பு"
    ]

    if any(word in q for word in student_words):
        info["student"] = True


    # --------------------------------------------------
    # DEPARTMENT DETECTION
    # --------------------------------------------------

    if (
        "cse" in q
        or "computer science" in q
        or "computer engineering" in q
        or "கணினி" in q
    ):
        info["department"] = "CSE"


    elif (
        "ai & ds" in q
        or "ai and ds" in q
        or "artificial intelligence and data science" in q
        or "data science" in q
    ):
        info["department"] = "AI & DS"


    elif (
        "information technology" in q
        or " i.t " in q
    ):
        info["department"] = "IT"


    elif (
        "cyber security" in q
        or "cybersecurity" in q
    ):
        info["department"] = "Cyber Security"


    elif (
        "ece" in q
        or "electronics and communication" in q
        or "எலக்ட்ரானிக்ஸ்" in q
    ):
        info["department"] = "ECE"


    elif (
        "eee" in q
        or "electrical and electronics" in q
        or "எலக்ட்ரிக்கல்" in q
    ):
        info["department"] = "EEE"


    elif (
        "mechanical" in q
        or "mech" in q
        or "மெக்கானிக்கல்" in q
    ):
        info["department"] = "Mechanical"


    elif (
        "automobile" in q
        or "automotive" in q
    ):
        info["department"] = "Automobile"


    elif (
        "civil" in q
        or "சிவில்" in q
    ):
        info["department"] = "Civil"


    elif (
        "biotechnology" in q
        or "biotech" in q
    ):
        info["department"] = "Biotechnology"


    elif (
        "agriculture" in q
        or "agri" in q
    ):
        info["department"] = "Agriculture"


    # --------------------------------------------------
    # YEAR DETECTION
    # --------------------------------------------------

    if (
        "1st year" in q
        or "first year" in q
        or "முதலாம் ஆண்டு" in q
    ):
        info["year"] = "1st Year"


    elif (
        "2nd year" in q
        or "second year" in q
        or "இரண்டாம் ஆண்டு" in q
    ):
        info["year"] = "2nd Year"


    elif (
        "3rd year" in q
        or "third year" in q
        or "மூன்றாம் ஆண்டு" in q
    ):
        info["year"] = "3rd Year"


    elif (
        "4th year" in q
        or "fourth year" in q
        or "நான்காம் ஆண்டு" in q
    ):
        info["year"] = "4th Year"


    # --------------------------------------------------
    # LOCATION DETECTION
    # --------------------------------------------------

    if (
        "tamil nadu" in q
        or "tamilnadu" in q
        or "தமிழ்நாடு" in q
    ):
        info["location"] = "Tamil Nadu"


    elif (
        "salem" in q
        or "சேலம்" in q
    ):
        info["location"] = "Salem"


    elif (
        "chennai" in q
        or "சென்னை" in q
    ):
        info["location"] = "Chennai"


    elif "coimbatore" in q:
        info["location"] = "Coimbatore"


    elif "erode" in q:
        info["location"] = "Erode"


    elif "kerala" in q:
        info["location"] = "Kerala"


    return info


# ==================================================
# CATEGORY DETECTION
# ==================================================

def detect_categories(query):

    q = query.lower()

    categories = []


    # JOBS

    job_words = [
        "job",
        "jobs",
        "career",
        "employment",
        "வேலை",
        "வேலைவாய்ப்பு",
        "பணி"
    ]

    if any(word in q for word in job_words):
        categories.append("Jobs")


    # INTERNSHIP

    internship_words = [
        "internship",
        "intern",
        "industrial training",
        "பயிற்சி",
        "இன்டர்ன்ஷிப்"
    ]

    if any(word in q for word in internship_words):
        categories.append("Internship")


    # EDUCATION

    education_words = [
        "scholarship",
        "education",
        "college fee",
        "study support",
        "உதவித்தொகை",
        "கல்வி"
    ]

    if any(word in q for word in education_words):
        categories.append("Education")


    # SKILLS

    skill_words = [
        "skill",
        "skills",
        "learn",
        "learning",
        "course",
        "courses",
        "technology",
        "திறன்",
        "கற்றுக்கொள்ள"
    ]

    if any(word in q for word in skill_words):
        categories.append("Skills")


    # GOVERNMENT

    government_words = [
        "government",
        "govt",
        "government scheme",
        "அரசு",
        "அரசாங்கம்",
        "அரசு திட்டம்"
    ]

    if any(word in q for word in government_words):
        categories.append("Government")


    return categories


# ==================================================
# SPECIFIC SKILL DETECTION
# ==================================================

def detect_specific_skill(query):

    q = query.lower()

    skills = [

        ("machine learning", "Machine Learning"),

        ("artificial intelligence", "Artificial Intelligence"),

        ("data science", "Data Science"),

        ("javascript", "JavaScript"),

        ("python", "Python"),

        ("java", "Java"),

        ("iot", "IoT"),

        ("embedded", "Embedded"),

        ("electronics", "Electronics"),

        ("electrical", "Electrical"),

        ("mechanical", "Mechanical"),

        ("civil", "Civil"),

        ("automobile", "Automobile"),

        ("biotechnology", "Biotechnology"),

        ("agriculture", "Agriculture")
    ]


    for keyword, skill in skills:

        if keyword in q:
            return skill


    return None


# ==================================================
# SERVICE SCORE
# ==================================================

def calculate_score(
    service,
    query,
    department,
    categories,
    specific_skill
):

    q = query.lower()

    title = (
        service.title or ""
    ).lower()

    description = (
        service.description or ""
    ).lower()

    category = (
        service.category or ""
    ).lower()

    score = 0


    # --------------------------------------------------
    # DEPARTMENT MATCH
    # --------------------------------------------------

    if service.departments:

        departments = [
            d.strip().lower()
            for d in service.departments.split(",")
        ]

        if (
            department
            and department.lower() in departments
        ):
            score += 50


    # --------------------------------------------------
    # CATEGORY MATCH
    # --------------------------------------------------

    if (
        "Jobs" in categories
        and category == "jobs"
    ):
        score += 50


    if (
        "Internship" in categories
        and category == "internship"
    ):
        score += 50


    if (
        "Education" in categories
        and category == "education"
    ):
        score += 50


    if (
        "Skills" in categories
        and category == "skills"
    ):
        score += 50


    if (
        "Government" in categories
        and category == "government"
    ):
        score += 50


    # --------------------------------------------------
    # SPECIFIC SKILL
    # --------------------------------------------------

    if specific_skill:

        skill = specific_skill.lower()

        if skill in title:
            score += 60

        if skill in description:
            score += 20


    # --------------------------------------------------
    # WORD MATCHING
    # --------------------------------------------------

    words = q.split()

    for word in words:

        if len(word) < 3:
            continue

        if word in title:
            score += 10

        elif word in description:
            score += 3


    return score


# ==================================================
# HOME PAGE
# ==================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==================================================
# PROFILE
# ==================================================

@app.route(
    "/profile",
    methods=["GET", "POST"]
)
def profile():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        department = request.form.get(
            "department",
            ""
        ).strip()

        year = request.form.get(
            "year",
            ""
        ).strip()

        location = request.form.get(
            "location",
            ""
        ).strip()


        if not name or not email:

            return """
            <h2>❌ Name and Email are required.</h2>

            <a href="/profile">
                Go Back
            </a>
            """


        user = User.query.filter_by(
            email=email
        ).first()


        if user:

            user.name = name
            user.department = department
            user.year = year
            user.location = location

        else:

            user = User(
                name=name,
                email=email,
                department=department,
                year=year,
                location=location
            )

            db.session.add(user)


        db.session.commit()


        session["user_id"] = user.id


        return redirect(
            url_for("profile_success")
        )


    return render_template(
        "profile.html"
    )


# ==================================================
# PROFILE SUCCESS
# ==================================================

@app.route("/profile-success")
def profile_success():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>Profile Saved</title>

        <style>

            body {
                font-family: Arial;
                background: #f4f7fb;
                text-align: center;
                padding: 80px;
            }

            .box {
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 20px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }

        </style>

    </head>

    <body>

        <div class="box">

            <h1>🎉 Profile Saved!</h1>

            <p>
                Your AI Bridge profile has been saved successfully.
            </p>

            <p>
                AI Bridge will now personalize your recommendations.
            </p>

            <a href="/">
                🏠 Go to AI Bridge
            </a>

        </div>

    </body>

    </html>
    """


# ==================================================
# AI RECOMMENDATION
# ==================================================

@app.route(
    "/ask",
    methods=["POST"]
)
def ask():

    query = request.form.get(
        "query",
        ""
    ).strip()


    if not query:

        return """
        <h3>
            ⚠️ Please enter your question.
        </h3>
        """


    # --------------------------------------------------
    # GET USER
    # --------------------------------------------------

    user = None

    user_id = session.get(
        "user_id"
    )


    if user_id:

        user = db.session.get(
            User,
            user_id
        )


    # --------------------------------------------------
    # UNDERSTAND QUESTION
    # --------------------------------------------------

    user_info = understand_user(
        query
    )

    categories = detect_categories(
        query
    )

    specific_skill = detect_specific_skill(
        query
    )


    # --------------------------------------------------
    # PROFILE DEFAULTS
    # --------------------------------------------------

    department = None
    year = None
    location = None


    if user:

        department = user.department
        year = user.year
        location = user.location


    # --------------------------------------------------
    # QUESTION OVERRIDES PROFILE
    # --------------------------------------------------

    if user_info["department"]:
        department = user_info["department"]


    if user_info["year"]:
        year = user_info["year"]


    if user_info["location"]:
        location = user_info["location"]


    # --------------------------------------------------
    # GET SERVICES
    # --------------------------------------------------

    services = Service.query.all()

    results = []


    # --------------------------------------------------
    # SCORE SERVICES
    # --------------------------------------------------

    for service in services:

        score = calculate_score(
            service,
            query,
            department,
            categories,
            specific_skill
        )


        # Profile department bonus

        if (
            user
            and department
            and service.departments
        ):

            departments = [
                d.strip().lower()
                for d in service.departments.split(",")
            ]


            if department.lower() in departments:
                score += 30


        # Year bonus

        if user and year:

            if service.category in [
                "Internship",
                "Education",
                "Skills"
            ]:
                score += 5


        results.append(
            (score, service)
        )


    results.sort(
        key=lambda x: x[0],
        reverse=True
    )


    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------

    if results:

        max_score = results[0][0]


        if max_score == 0:

            top_results = results[:3]

        else:

            top_results = [
                item
                for item in results
                if item[0] > 0
            ][:5]

    else:

        top_results = []


    if not top_results:

        return """
        <div style="
            padding:20px;
            background:#fff7ed;
            border-radius:12px;
        ">

            <h3>
                🔎 No matching opportunity found.
            </h3>

            <p>
                Try asking about jobs,
                internships, scholarships
                or skills.
            </p>

        </div>
        """


    # --------------------------------------------------
    # RESULT PAGE
    # --------------------------------------------------

    html = """

    <div class="results">

        <h2>
            🤖 AI Bridge Recommendations
        </h2>

    """


    # Profile information

    if user:

        html += f"""

        <div style="
            padding:15px;
            margin-bottom:20px;
            background:#eef6ff;
            border-radius:10px;
        ">

            <b>👤 Personalized for:</b>
            {escape(user.name)}

            <br>

            🎓 Department:
            {escape(user.department or "Not set")}

            <br>

            📚 Year:
            {escape(user.year or "Not set")}

            <br>

            📍 Location:
            {escape(user.location or "Not set")}

        </div>

        """

    else:

        html += """

        <div style="
            padding:15px;
            margin-bottom:20px;
            background:#fff7ed;
            border-radius:10px;
        ">

            👤 No profile detected.

            <br><br>

            <a href="/profile">
                Create Profile
            </a>

        </div>

        """


    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    for index, (
        score,
        service
    ) in enumerate(
        top_results,
        start=1
    ):

        html += f"""

        <div style="
            padding:20px;
            margin-bottom:15px;
            border:1px solid #ddd;
            border-radius:12px;
            background:white;
        ">

            <h3>
                {index}. {escape(service.title)}
            </h3>

            <p>

                <b>
                    Category:
                </b>

                {escape(service.category)}

            </p>


            <p>
                {escape(
                    service.description or ""
                )}
            </p>


            <p>

                <b>
                    Eligibility:
                </b>

                {escape(
                    service.eligibility
                    or "Check official website"
                )}

            </p>


            <p>

                <b>
                    Documents:
                </b>

                {escape(
                    service.documents
                    or "Check official website"
                )}

            </p>


            <p>

                <b>
                    How to apply:
                </b>

                {escape(
                    service.how_to_apply
                    or "Visit the official website"
                )}

            </p>

        """


        if service.official_link:

            html += f"""

            <p>

                <a
                    href="{escape(service.official_link)}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    🔗 Official Website
                </a>

            </p>

            """


        html += """

        </div>

        """


    html += """

    </div>

    """


    return html


# ==================================================
# OPPORTUNITY SEARCH
# ==================================================

@app.route("/opportunities")
def opportunities():

    department = request.args.get(
        "department",
        ""
    ).strip()

    category = request.args.get(
        "category",
        ""
    ).strip()

    query = request.args.get(
        "q",
        ""
    ).strip().lower()


    services = Service.query.all()

    results = []


    # --------------------------------------------------
    # FILTER SERVICES
    # --------------------------------------------------

    for service in services:

        # Department filter

        if department:

            if not service.departments:
                continue


            departments = [
                d.strip().lower()
                for d in service.departments.split(",")
            ]


            if department.lower() not in departments:
                continue


        # Category filter

        if category:

            if service.category.lower() != category.lower():
                continue


        # Search filter

        if query:

            searchable_text = (
                (service.title or "")
                + " "
                + (service.description or "")
                + " "
                + (service.category or "")
            ).lower()


            if query not in searchable_text:
                continue


        results.append(service)


    # --------------------------------------------------
    # SEARCH PAGE
    # --------------------------------------------------

    html = """

    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <title>
            AI Bridge Opportunities
        </title>


        <style>

            * {
                box-sizing: border-box;
            }


            body {

                margin: 0;

                font-family: Arial, sans-serif;

                background:
                    linear-gradient(
                        135deg,
                        #eef4ff,
                        #f8fbff
                    );

                color: #1e293b;

            }


            .header {

                background:
                    linear-gradient(
                        135deg,
                        #2563eb,
                        #4f46e5
                    );

                color: white;

                text-align: center;

                padding: 30px 20px;

            }


            .container {

                max-width: 950px;

                margin: 30px auto;

                padding: 20px;

            }


            .search-box {

                background: white;

                padding: 25px;

                border-radius: 18px;

                box-shadow:
                    0 8px 25px
                    rgba(0,0,0,0.08);

                margin-bottom: 25px;

            }


            input,
            select {

                width: 100%;

                padding: 13px;

                margin-top: 8px;

                margin-bottom: 15px;

                border:
                    1px solid #cbd5e1;

                border-radius: 9px;

                font-size: 15px;

            }


            button {

                width: 100%;

                padding: 14px;

                border: none;

                border-radius: 10px;

                background: #2563eb;

                color: white;

                font-size: 16px;

                font-weight: bold;

                cursor: pointer;

            }


            button:hover {

                background: #1d4ed8;

            }


            .card {

                background: white;

                padding: 22px;

                margin-bottom: 15px;

                border-radius: 15px;

                box-shadow:
                    0 5px 20px
                    rgba(0,0,0,0.07);

            }


            .tag {

                display: inline-block;

                padding: 6px 12px;

                background: #dbeafe;

                border-radius: 20px;

                font-size: 13px;

            }


            .official {

                display: inline-block;

                margin-top: 8px;

                padding: 10px 15px;

                background: #16a34a;

                color: white;

                text-decoration: none;

                border-radius: 8px;

            }


            .back {

                color: white;

                text-decoration: none;

            }


        </style>

    </head>


    <body>


        <div class="header">

            <h1>
                🌉 AI Bridge
            </h1>

            <p>
                Find Opportunities
            </p>

            <a
                class="back"
                href="/"
            >
                ← Back to AI Bridge
            </a>

        </div>


        <div class="container">


            <div class="search-box">

                <h2>
                    🔎 Search Opportunities
                </h2>


                <form
                    method="GET"
                    action="/opportunities"
                >


                    <label>
                        Department
                    </label>


                    <select
                        name="department"
                    >

                        <option value="">
                            All Departments
                        </option>

                        <option value="CSE">
                            CSE
                        </option>

                        <option value="AI & DS">
                            AI & DS
                        </option>

                        <option value="IT">
                            IT
                        </option>

                        <option value="Cyber Security">
                            Cyber Security
                        </option>

                        <option value="ECE">
                            ECE
                        </option>

                        <option value="EEE">
                            EEE
                        </option>

                        <option value="Mechanical">
                            Mechanical
                        </option>

                        <option value="Automobile">
                            Automobile
                        </option>

                        <option value="Civil">
                            Civil
                        </option>

                        <option value="Biotechnology">
                            Biotechnology
                        </option>

                        <option value="Agriculture">
                            Agriculture
                        </option>

                    </select>


                    <label>
                        Category
                    </label>


                    <select
                        name="category"
                    >

                        <option value="">
                            All Categories
                        </option>

                        <option value="Jobs">
                            💼 Jobs
                        </option>

                        <option value="Internship">
                            🧑‍💻 Internship
                        </option>

                        <option value="Skills">
                            📚 Skills
                        </option>

                        <option value="Education">
                            🎓 Education
                        </option>

                        <option value="Government">
                            🇮🇳 Government
                        </option>

                    </select>


                    <label>
                        Search
                    </label>


                    <input
                        type="text"
                        name="q"
                        placeholder="Python, AI, internship..."
                    >


                    <button type="submit">
                        🔎 Search
                    </button>


                </form>

            </div>


    """


    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------

    if not results:

        html += """

            <div class="card">

                <h3>
                    🔎 No opportunities found
                </h3>

                <p>
                    Try another department,
                    category or search keyword.
                </p>

            </div>

        """


    else:

        html += f"""

            <p>
                Found
                <b>{len(results)}</b>
                opportunities.
            </p>

        """


        for service in results:

            html += f"""

            <div class="card">

                <h2>
                    {escape(service.title)}
                </h2>


                <span class="tag">
                    {escape(service.category)}
                </span>


                <p>
                    {escape(
                        service.description or ""
                    )}
                </p>


                <p>

                    <b>
                        Eligibility:
                    </b>

                    {escape(
                        service.eligibility
                        or "Check official website"
                    )}

                </p>


                <p>

                    <b>
                        How to apply:
                    </b>

                    {escape(
                        service.how_to_apply
                        or "Check official website"
                    )}

                </p>

            """


            if service.official_link:

                html += f"""

                <a
                    class="official"
                    href="{escape(service.official_link)}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    🔗 Official Website
                </a>

                """


            html += """

            </div>

            """


    html += """

        </div>

    </body>

    </html>

    """


    return html


# ==================================================
# CREATE DATABASE
# ==================================================

with app.app_context():

    db.create_all()


# ==================================================
# RUN APPLICATION
# ==================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )