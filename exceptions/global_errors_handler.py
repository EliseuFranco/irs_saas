from flask import jsonify
from dtos.response_dto import ResponseDto
from controllers.auth_controller import auth_bp


def register_error_handler(app):
    
    @app.errorhandler(404)
    def not_found(e):
        response = ResponseDto(400, "", "Recurso nao enontrado")
        return jsonify(response.to_json()), 400
    
    @app.errorhandler(500)
    def server_error():
        response = ResponseDto(500, "", "houve um erro na comunicação com o servidor")
        return jsonify(response), 500
    

def handle_field_error(e):
    response = {"status": 400, "message": str(e)}
    return jsonify(response), 400
