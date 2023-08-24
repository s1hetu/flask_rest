from flask import Blueprint, request, Response, jsonify
from flask_restful import Api, Resource
from QA import db

from .models import User
from .schemas import user_request_schema, UserRequestSchema, create_tag_schema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_blueprint = Blueprint('user', __name__)

user_api = Api(user_blueprint)


class Home(Resource):
    def get(self):
        pass


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        user_data = UserRequestSchema().load(data)
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        response = user_request_schema.dump(user)
        return {"message": "User added successfully.", "status_code": 201,
                "data": response}  # return jsonify({"message": "User added successfully.", "status_code": 201, "data": response})


user_api.add_resource(UserRegistration, '/signup')


class Login(Resource):
    access_token = create_access_token()

# class CreateTag(Resource):
#     def post(self):
#         data = request.get_json()
#         tag_data = create_tag_schema.load(data)
#         tag =
