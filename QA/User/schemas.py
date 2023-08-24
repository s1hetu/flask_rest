from marshmallow import fields, validate
from QA import marshmallow


class UserRequestSchema(marshmallow.Schema):
    username = fields.Str(required=True, validate=[validate.Length(min=1, max=50)])
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=[validate.Length(min=3, max=9)])


user_request_schema = UserRequestSchema()


class CreateTagSchema(marshmallow.Schema):
    tag = fields.Str(required=True, validate=[validate.Length(min=1, max=20)])


create_tag_schema = CreateTagSchema()