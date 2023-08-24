Schema


```python 
# inside schemas.py
user_request_schema = UserRequestSchema() 
1. user_data = user_request_schema.load(data) 

                    OR 

2. user_data = UserRequestSchema().load(data)
```

```python
question_request_schema = QuestionRequestSchema() -> Single object
questions_request_schema = QuestionRequestSchema(many=True) -> Queryset
```