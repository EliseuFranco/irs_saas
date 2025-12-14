import os



def db_config(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:%40Samulolo26@localhost:5432/irs_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

