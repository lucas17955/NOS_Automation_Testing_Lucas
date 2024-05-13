import jsonschema

def validate_response_schema(response, schema):
    """
    Validates the response against the provided JSON schema.
    """
    jsonschema.validate(response.json(), schema)