from app import app
from database import db, Service


services = [

    # ==================================================
    # CSE
    # ==================================================

    Service(
        title="Python Programming Skills",
        category="Skills",
        description="Learn Python programming, problem solving, automation and software development.",
        eligibility="Students and beginners interested in programming.",
        documents="Usually no documents required.",
        how_to_apply="Use recognized learning platforms and practice projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="CSE"
    ),

    Service(
        title="CSE Software Development Internship",
        category="Internship",
        description="Software development internship opportunities for CSE students.",
        eligibility="Computer Science students and beginners with programming knowledge.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship portals and company career pages.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="CSE"
    ),

    Service(
        title="CSE Software Development Jobs",
        category="Jobs",
        description="Career opportunities related to software development and programming.",
        eligibility="Candidates with relevant software development skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified company career pages and employment portals.",
        official_link="https://www.ncs.gov.in/",
        departments="CSE"
    ),


    # ==================================================
    # AI & DATA SCIENCE
    # ==================================================

    Service(
        title="Artificial Intelligence and Data Science Skills",
        category="Skills",
        description="Learn artificial intelligence, machine learning, data analysis and data science.",
        eligibility="Students and beginners interested in AI and data.",
        documents="Usually no documents required.",
        how_to_apply="Start with recognized courses and practical projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="AI & DS"
    ),

    Service(
        title="AI and Data Science Internship",
        category="Internship",
        description="Internship opportunities related to artificial intelligence, machine learning and data science.",
        eligibility="Students with basic programming or data knowledge.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="AI & DS"
    ),

    Service(
        title="AI and Data Science Jobs",
        category="Jobs",
        description="Career opportunities in artificial intelligence, machine learning and data science.",
        eligibility="Candidates with relevant AI or data science skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified company career pages and employment portals.",
        official_link="https://www.ncs.gov.in/",
        departments="AI & DS"
    ),


    # ==================================================
    # IT
    # ==================================================

    Service(
        title="Information Technology Skills",
        category="Skills",
        description="Develop skills in web development, databases, cloud computing and programming.",
        eligibility="IT students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Learn through recognized courses and practical projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="IT"
    ),

    Service(
        title="Information Technology Internship",
        category="Internship",
        description="Internship opportunities in web development, software and IT services.",
        eligibility="IT students and candidates with basic technical skills.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship portals and company career pages.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="IT"
    ),

    Service(
        title="Information Technology Jobs",
        category="Jobs",
        description="Career opportunities in software, web development, IT support and technology.",
        eligibility="Candidates with relevant IT skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and company career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="IT"
    ),


    # ==================================================
    # CYBER SECURITY
    # ==================================================

    Service(
        title="Cyber Security Skills",
        category="Skills",
        description="Learn cybersecurity fundamentals, networking, security awareness and ethical security concepts.",
        eligibility="Students interested in cybersecurity.",
        documents="Usually no documents required.",
        how_to_apply="Begin with recognized cybersecurity learning programs.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Cyber Security"
    ),

    Service(
        title="Cyber Security Internship",
        category="Internship",
        description="Internship opportunities related to cybersecurity and information security.",
        eligibility="Students with basic networking or security knowledge.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Cyber Security"
    ),

    Service(
        title="Cyber Security Jobs",
        category="Jobs",
        description="Career opportunities in cybersecurity and information security.",
        eligibility="Candidates with relevant cybersecurity skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified company career pages and employment portals.",
        official_link="https://www.ncs.gov.in/",
        departments="Cyber Security"
    ),


    # ==================================================
    # ECE
    # ==================================================

    Service(
        title="IoT and Embedded Skills",
        category="Skills",
        description="Learn IoT, embedded systems, microcontrollers and electronics fundamentals.",
        eligibility="ECE students and electronics beginners.",
        documents="Usually no documents required.",
        how_to_apply="Use recognized technical learning programs and projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="ECE"
    ),

    Service(
        title="ECE Electronics Internship",
        category="Internship",
        description="Internship opportunities in electronics, communication, embedded systems and IoT.",
        eligibility="ECE students with basic electronics knowledge.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="ECE"
    ),

    Service(
        title="ECE Engineering Jobs",
        category="Jobs",
        description="Career opportunities in electronics, communication, embedded systems and IoT.",
        eligibility="Candidates with relevant electronics skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified company career pages and employment portals.",
        official_link="https://www.ncs.gov.in/",
        departments="ECE"
    ),


    # ==================================================
    # EEE
    # ==================================================

    Service(
        title="Electrical Engineering Skills",
        category="Skills",
        description="Learn electrical systems, power systems, electrical machines and basic control concepts.",
        eligibility="EEE students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Use recognized technical learning programs and projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="EEE"
    ),

    Service(
        title="EEE Engineering Internship",
        category="Internship",
        description="Internship opportunities in electrical engineering and power-related fields.",
        eligibility="EEE students with basic electrical knowledge.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="EEE"
    ),

    Service(
        title="EEE Engineering Jobs",
        category="Jobs",
        description="Career opportunities in electrical engineering and power systems.",
        eligibility="Candidates with relevant electrical engineering skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and company career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="EEE"
    ),


    # ==================================================
    # MECHANICAL
    # ==================================================

    Service(
        title="Mechanical Engineering Skills",
        category="Skills",
        description="Develop skills in CAD, manufacturing, design and mechanical engineering.",
        eligibility="Mechanical students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Learn through recognized technical courses and projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Mechanical"
    ),

    Service(
        title="Mechanical Engineering Internship",
        category="Internship",
        description="Internship opportunities in mechanical design, manufacturing and engineering.",
        eligibility="Mechanical engineering students.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Mechanical"
    ),

    Service(
        title="Mechanical Engineering Jobs",
        category="Jobs",
        description="Career opportunities in mechanical design, manufacturing and engineering.",
        eligibility="Candidates with relevant mechanical engineering skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and company career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="Mechanical"
    ),


    # ==================================================
    # AUTOMOBILE
    # ==================================================

    Service(
        title="Automobile Engineering Skills",
        category="Skills",
        description="Learn automobile systems, vehicle technology, CAD and automotive fundamentals.",
        eligibility="Automobile students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Learn through recognized technical courses and practical projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Automobile"
    ),

    Service(
        title="Automobile Engineering Internship",
        category="Internship",
        description="Internship opportunities in automobile engineering and vehicle technology.",
        eligibility="Automobile engineering students.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Automobile"
    ),

    Service(
        title="Automobile Engineering Jobs",
        category="Jobs",
        description="Career opportunities in automobile engineering and automotive technology.",
        eligibility="Candidates with relevant automobile engineering skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and company career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="Automobile"
    ),


    # ==================================================
    # CIVIL
    # ==================================================

    Service(
        title="Civil Engineering Skills",
        category="Skills",
        description="Learn civil design, surveying, construction and CAD fundamentals.",
        eligibility="Civil engineering students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Use recognized technical courses and practical projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Civil"
    ),

    Service(
        title="Civil Engineering Internship",
        category="Internship",
        description="Internship opportunities in construction, civil design and surveying.",
        eligibility="Civil engineering students.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and company career portals.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Civil"
    ),

    Service(
        title="Civil Engineering Jobs",
        category="Jobs",
        description="Career opportunities in civil engineering, construction and infrastructure.",
        eligibility="Candidates with relevant civil engineering skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and company career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="Civil"
    ),


    # ==================================================
    # BIOTECHNOLOGY
    # ==================================================

    Service(
        title="Biotechnology Skills",
        category="Skills",
        description="Learn biotechnology fundamentals, laboratory concepts, data analysis and life science skills.",
        eligibility="Biotechnology students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Use recognized learning programs and academic projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Biotechnology"
    ),

    Service(
        title="Biotechnology Internship",
        category="Internship",
        description="Internship opportunities related to biotechnology and life science fields.",
        eligibility="Biotechnology and related students.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and organization career pages.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Biotechnology"
    ),

    Service(
        title="Biotechnology Jobs",
        category="Jobs",
        description="Career opportunities in biotechnology and related life science areas.",
        eligibility="Candidates with relevant biotechnology education and skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and organization career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="Biotechnology"
    ),


    # ==================================================
    # AGRICULTURE
    # ==================================================

    Service(
        title="Agriculture Technology Skills",
        category="Skills",
        description="Learn modern agriculture technology, data-based farming and agricultural fundamentals.",
        eligibility="Agriculture students and beginners.",
        documents="Usually no documents required.",
        how_to_apply="Use recognized agricultural learning programs and practical projects.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Agriculture"
    ),

    Service(
        title="Agriculture Internship",
        category="Internship",
        description="Internship opportunities related to agriculture, agricultural technology and rural development.",
        eligibility="Agriculture and related students.",
        documents="Resume and educational details may be required.",
        how_to_apply="Search verified internship and organization career pages.",
        official_link="https://www.skillindiadigital.gov.in/",
        departments="Agriculture"
    ),

    Service(
        title="Agriculture Jobs",
        category="Jobs",
        description="Career opportunities in agriculture, agricultural technology and related fields.",
        eligibility="Candidates with relevant agriculture education and skills.",
        documents="Resume and educational details.",
        how_to_apply="Apply through verified employment and organization career portals.",
        official_link="https://www.ncs.gov.in/",
        departments="Agriculture"
    ),


    # ==================================================
    # COMMON SERVICES
    # ==================================================

    Service(
        title="Student Scholarship Support",
        category="Education",
        description="Find scholarship and education-support opportunities for eligible students.",
        eligibility="Eligibility depends on the specific scholarship.",
        documents="Commonly academic, identity and income-related documents may be required depending on the scheme.",
        how_to_apply="Check the official scholarship portal and scheme requirements.",
        official_link="https://scholarships.gov.in/",
        departments="CSE,AI & DS,IT,Cyber Security,ECE,EEE,Mechanical,Automobile,Civil,Biotechnology,Agriculture"
    ),

    Service(
        title="Government Internship Opportunities",
        category="Government",
        description="Explore government internship and learning opportunities. Availability and eligibility vary by program.",
        eligibility="Depends on the individual government program.",
        documents="Depends on the program.",
        how_to_apply="Check the official government program website for current openings.",
        official_link="https://www.mygov.in/",
        departments="CSE,AI & DS,IT,Cyber Security,ECE,EEE,Mechanical,Automobile,Civil,Biotechnology,Agriculture"
    )
]


with app.app_context():

    print()
    print("==========================================")
    print("🚀 AI BRIDGE DATABASE UPDATE")
    print("==========================================")

    # Clear old services
    Service.query.delete()

    # Add new services
    db.session.add_all(services)

    db.session.commit()

    print()
    print("✅ Database updated successfully!")
    print()
    print("Total services:", Service.query.count())
    print()
    print("Departments:")
    print("1. CSE")
    print("2. AI & DS")
    print("3. IT")
    print("4. Cyber Security")
    print("5. ECE")
    print("6. EEE")
    print("7. Mechanical")
    print("8. Automobile")
    print("9. Civil")
    print("10. Biotechnology")
    print("11. Agriculture")
    print()
    print("==========================================")