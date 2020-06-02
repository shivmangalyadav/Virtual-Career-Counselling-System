import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_jwt import JWT, jwt_required, current_identity
from api.course_channel.userauth import authenticate, identity

from admin.database import Base, engine
from admin import Admin
from api.course_channel.courses import channelmod


app = Flask(__name__, template_folder="admin/templates")
app.config['SECRET_KEY'] = 'hdfhik snak hnahndlkndg dfigjod fsadfd;dsf'

app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)

app.register_blueprint(Admin, url_prefix="/admin")
app.register_blueprint(channelmod, url_prefix='/channel')


if __name__ == "__main__":
    app.run(debug=True)
