from db.connection import db
from models.users import Users


def exist_by_id(user_id):
    return Users.query.filter_by(id = user_id).first_or_404()

