# from flask import Flask
# from admin import app
# from api import app 

import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet

from admin.database import Base, engine


from flask_jwt import JWT, jwt_required, current_identity
from api.course_channel.userauth import authenticate, identity

from admin.blueprints.Auth.login import Adminlogin
from admin.blueprints.Public.index import Adminindex
from admin.blueprints.Counselling.dataUpload import universitydataUpload
from admin.blueprints.Counselling.dataDelete import universitydataDelete
from admin.blueprints.Auth.logout import Adminlogout

from api.course_channel.courses import channelmod


app = Flask(__name__, template_folder="admin/templates")
app.config['SECRET_KEY'] = 'hdfhik snak hnahndlkndg dfigjod fsadfd;dsf'

app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)

app.register_blueprint(Adminlogin, url_prefix="/admin")
app.register_blueprint(Adminindex, url_prefix="/admin")
app.register_blueprint(universitydataUpload, url_prefix="/admin")
app.register_blueprint(universitydataDelete, url_prefix="/admin")
app.register_blueprint(Adminlogout, url_prefix="/admin")

app.register_blueprint(channelmod, url_prefix='/channel')



if __name__ == "__main__":
    app.run(debug=True)
