from marshmallow import validate, Schema, fields
# from flask_marshmallow import fields
# from flask_marshmallow import Schema = from marshmallow import Schema
from QA import marshmallow
from QA.Question.models import Question


class QuestionRequestSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        include_relationships = True


question_request_schema = QuestionRequestSchema()
questions_request_schema = QuestionRequestSchema(many=True)
