from flask_jwt_extended import (create_access_token)


def authenticate(login_data):
    access_token = create_access_token(identity = login_data['UserEmail'])

    return access_token
