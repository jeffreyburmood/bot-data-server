""" this file contains the class definition for the test case base contents """

from jsonschema import ValidationError, SchemaError
from jsonschema import validators
import jsonschema
from jsonschema.validators import Draft202012Validator


class MyObject:
    pass

class List(list):
    def get(self, item):
        return self[0]

def is_my_object(checker, instance):
    return (
        Draft202012Validator.TYPE_CHECKER.is_type(instance, "object") or
        isinstance(instance, MyObject)
    )

class Contract:
    def __init__(self, logger):
        self.logger = logger

        self.type_checker = Draft202012Validator.TYPE_CHECKER.redefine(
            "object", is_my_object
        )

        self.CustomValidator = validators.extend(
            Draft202012Validator,
            type_checker=self.type_checker,
        )
        self.validator = self.CustomValidator(schema={"type": "object"})

    def validate_schema(self, json_file, schema_file) -> bool:
        try:
            #jsonschema.Draft202012Validator(json_file, schema_file)
            jsonschema.Draft3Validator(json_file, schema_file)
            #jsonschema.validate(json_file, schema_file)
            return True

        except ValidationError as ve:
            self.logger.error(f"schema validation error for file {schema_file}, looks like {ve}")
            return False

        except SchemaError as se:
            self.logger.error(f"schema format error for file {schema_file}, looks like {se}")
            return False

        except Exception as e:
            self.logger.error(f"an exception occurred during schema validation, looks like {e}")
            return False


