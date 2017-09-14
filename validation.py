from voluptuous.schema_builder import Schema, Required


class Validator:

    _post_schema = Schema({
        Required('name'): str,
        Required('team'): str,
        Required('position'): str
    })

    _schema = Schema({Required('_id'): int})

    @classmethod
    def validate(cls, data):
        return cls._schema(data)

    @classmethod
    def validate_post(cls, data):
        return cls._post_schema(data)
