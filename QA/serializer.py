from flask import request


class Serializer:

    @staticmethod
    def load_data(schema):
        response = request.get_json()

        if not response:
            return False, None
        try:
            data = schema.load(response)
            return True, data
        except Exception as e:
            return False, e.messages


    @staticmethod
    def dump_data(schema, data, extra_data=None):
        data = schema.dump(data)
        if extra_data:
            data.update(extra_data)
        return data
