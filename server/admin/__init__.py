# import datetime
# from flask import Flask, render_template, request, redirect, url_for, session
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from cryptography.fernet import Fernet

# from admin.blueprints.Auth.login import Adminlogin
# from admin.blueprints.Public.index import Adminindex
# from admin.blueprints.Counselling.dataUpload import universitydataUpload
# from admin.blueprints.Counselling.dataDelete import universitydataDelete
# from admin.blueprints.Auth.logout import Adminlogout
# from admin.database import Base, engine


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hdfhik snak hnahndlkndg dfigjod fsadfd;dsf'

# app.register_blueprint(Adminlogin, url_prefix="/admin")
# app.register_blueprint(Adminindex, url_prefix="/admin")
# app.register_blueprint(universitydataUpload, url_prefix="/admin")
# app.register_blueprint(universitydataDelete, url_prefix="/admin")
# app.register_blueprint(Adminlogout, url_prefix="/admin")
