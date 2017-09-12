from voluptuous.schema_builder import Schema, Optional, Required


class Validator:

    _schema = Schema({
        Optional('_id'): int,
        Required('name'): str,
        Required('team'): str,
        Required('position'): str
    })

    _post_schema = Schema({Required('_id'): int})

    @classmethod
    def validate(cls, data):
        return cls._schema(data)

    @classmethod
    def validate_post(cls, data):
        return cls._schema(data)
