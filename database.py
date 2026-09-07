from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100)
    )

    year = db.Column(
        db.String(50)
    )

    location = db.Column(
        db.String(100)
    )


class Service(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    eligibility = db.Column(
        db.Text
    )

    documents = db.Column(
        db.Text
    )

    how_to_apply = db.Column(
        db.Text
    )

    official_link = db.Column(
        db.String(500)
    )

    departments = db.Column(
        db.String(500)
    )