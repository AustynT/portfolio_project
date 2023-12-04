from .requests.login_request_schema import LoginRequestSchema
from .requests.registration_request_schema import RegistrationRequestSchema
from .responses.registration_response_schema import RegistrationResponseSchema
from .responses.login_response_schema import LoginResponseSchema


class AuthSchema:
    """
    Class for validating auth data.

    Attributes:
        login_request_schema (LoginRequestSchema): The schema for validating login data.
        registration_request_schema (RegistrationRequestSchema): The schema for validating registration data.
        registration_response_schema (RegistrationResponseSchema): The schema for validating registration data.
        login_response_schema (LoginResponseSchema): The schema for validating login data.
    """
    login_request_schema = LoginRequestSchema()
    registration_request_schema = RegistrationRequestSchema()
    registration_response_schema = RegistrationResponseSchema()
    login_response_schema = LoginResponseSchema()

    def get_request_schemas(self):
        """
        Return the request schemas.

        Returns:
            dict: The request schemas.
        """
        return {
            "login": self.login_request_schema,
            "register": self.registration_request_schema
        }

    def get_response_schemas(self):
        """
        Return the response schemas.

        Returns:
            dict: The response schemas.
        """
        return {
            "login": self.login_response_schema,
            "register": self.registration_response_schema
        }
