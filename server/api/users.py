from flask import request, jsonify, Flask, Blueprint
from cryptography.fernet import Fernet
from flask_jwt_extended import jwt_required, get_jwt_identity, JWTManager
from database import Users
from api import auth

user = Users()
User = Blueprint('user', __name__)

f = Fernet("ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=")

@User.route('/signin', methods=['GET', 'POST'])
def SignIn():
    data = request.get_json()
    print("Email:", data['email'])
    print("Password:", data['password'])

    login_data = user.signin(data)

    if (login_data):
        pwd = f.decrypt(login_data['UserPassword'].encode()).decode()
        if pwd == data['password']:
            access_token = auth.authenticate(login_data)

            return jsonify( {'access_token': access_token, 'msg': 'Login Successful.', 'status': True})
        else:
            return jsonify({'msg': 'Incorrect passowrd', 'status': False})
    else:
        return jsonify({'msg': "Incorrect Email Address", 'status': False})

@User.route('/signup', methods=['GET', 'POST'])
def SignUP():
    data = request.get_json()
    token = f.encrypt(data['password'].encode())
    
    msg = user.signup(data, token)
    return jsonify(msg)

@User.route('/profile')
@jwt_required
def Profile():
    user_email = get_jwt_identity()
    
    user_data = user.profile(user_email)
    print(user_data)

    return jsonify(user_data)

