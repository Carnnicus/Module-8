import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = 'This field cannot be empty'
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = 'This field cannot be empty'
    )

    def post(self):
        tabla = UserRegister.parser.parse_args()

        if UserModel.find_by_username(tabla['username']):
            return {'message': 'El usuario ya existe'}, 400

        user = UserModel(**tabla) #Se puede utilizar (**tabla) para unpackear
        user.save_to_db()

        return {'message': 'User created succesfully'}, 201
