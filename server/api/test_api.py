from datetime import timedelta
from flask import Blueprint, Response, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required


class TestApi:
    """
    API testing shit
    """

    def __init__(self):
        self.bp_test = Blueprint('test', __name__, url_prefix='/test')
        self.bp_test.route(
            '/', methods=['GET'])(self.get_test)
        self.bp_test.route(
            '/', methods=['POST'])(self.create_test)
        self.bp_test.route('/<int:test_id>',
                           methods=['GET'],  endpoint="get_test_by_id")(self.get_test_by_id)
        self.bp_test.route('/<int:test_id>',
                           methods=['PUT'],  endpoint="update_test")(self.update_test)
        self.bp_test.route(
            '/<int:project_id>', methods=['DELETE'], endpoint="delete_project")(self.delete_test)

    def get_test(self) -> Response:
        headers = self.create_header_tokens(1)
        print('here we are getting tests')

        response = make_response(
            jsonify({"message": "we have reached the get tests api"}))

        response.headers.set(
            'Authorization', f'{headers["Authorization"]}')
        response.headers.set(
            'Refresh-Token', f'{headers["Refresh-Token"]}')
        return response

    def get_test_by_id(self, test_id) -> Response:
        print('getting tests by id:', test_id)
        return jsonify({'message': "we have reached the tests"}), 200

    def create_test(self) -> Response:
        print('creating test')
        return jsonify({'message': "we have reached the tests"}), 200

    def update_test(self) -> Response:
        print('updating test')
        return jsonify({'message': "we have reached the tests"}), 200

    def delete_test(self) -> Response:
        print('deleting test')
        return jsonify({'message': "we have reached the tests"}), 200

    def create_header_tokens(self, user_id) -> tuple[str, str]:
        """
        Create access and refresh tokens for the given user ID.

        Parameters:
            user_id (str): The ID of the user.

        Returns:
            tuple: A tuple containing the access token and refresh token.
        """
        access_token = create_access_token(
            identity=user_id, expires_delta=timedelta(hours=1))
        refresh_token = create_refresh_token(
            identity=user_id, expires_delta=timedelta(days=30))
        return {
            'Authorization': f'Bearer {access_token}',
            'Refresh-Token': f'Bearer {refresh_token}'
        }
