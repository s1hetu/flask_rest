from .schemas import question_request_schema, questions_request_schema
from flask import Blueprint, request, Response, jsonify
from flask_restful import Api, Resource
from .models import Question
from QA.serializer import Serializer
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
question_blueprint = Blueprint('question', __name__)

question_api = Api(question_blueprint)


class AllQuestions(Resource):
    def get(self):
        questions = Question.query.all()
        return Serializer.dump_data(schema=questions_request_schema, data=questions)


question_api.add_resource(AllQuestions, '/questions')


