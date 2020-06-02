# import datetime
# from flask import Flask
# from flask_jwt import JWT, jwt_required, current_identity
# from api.course_channel.userauth import authenticate, identity

# from api.course_channel.courses import channelmod
# from admin.database import Base, engine


# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'super-secret'
# jwt = JWT(app, authenticate, identity)

# app.register_blueprint(channelmod, url_prefix='/channel')

