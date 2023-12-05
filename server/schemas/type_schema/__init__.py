from marshmallow import Schema, fields, validate


class TypeSchema(Schema):
    """
    Schema class for validating types.
    """
    id = fields.Integer(dump_only=True)
    name = fields.String(
        required=True, validate=validate.Length(min=1, max=50))
    description = fields.String(
        required=True, validate=validate.Length(min=1, max=255))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def get_request_schemas(self):
        """
        Returns a dictionary of request schemas.
        """
        return {
            'create_type': self,
            'update_type': self
        }

    def get_response_schemas(self):
        """
        Returns a dictionary of response schemas.
        """
        return {
            'type': self,
            'types': self
        }
