from flask import Flask
from controllers.auth_controller import auth_bp
from exceptions.global_errors_handler import register_error_handler, handle_field_error
from flask_cors import CORS
from db.config import  db_config
from db.connection import db
from exceptions.field_not_valid_exception import FieldNotValidError



app = Flask(__name__)
CORS(app=app, allow_headers="*",origins=["http://127.0.0.1:5500"]) #Permite que outras origens acedam aos recursos da API
db_config(app=app)# Cria a conexão com a base de dados
db.init_app(app=app)


app.register_blueprint(auth_bp, url_prefix="/auth")
register_error_handler(app)
app.register_error_handler(FieldNotValidError, handle_field_error)


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True)