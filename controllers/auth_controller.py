from flask import Blueprint, jsonify, request
from db.connection import db
from models.users import Users
from repository.users_repository import exist_by_id
from services.users_service import create_user
from dtos.user_request_dto import UserRequestDto
from exceptions.field_not_valid_exception import FieldNotValidError


auth_bp = Blueprint('auth',__name__)


@auth_bp.post("/login")
def login():
    new_user = UserRequestDto("ecece", "example@gmail.com", "1234567")
    return jsonify({"status": 'OK, tudo a funcionar'}), 200


@auth_bp.post("/register")
def register():
    return jsonify({"msg": "This is the register view"})


# @auth_bp.errorhandler(FieldNotValidError)
# def error(e):
#     return jsonify({'erro': 'Erro de validação de campos'}), 400