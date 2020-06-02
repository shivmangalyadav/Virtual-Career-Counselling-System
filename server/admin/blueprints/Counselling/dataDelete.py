from flask import Blueprint, Flask, render_template, abort, redirect, session, url_for,request
from jinja2 import TemplateNotFound
from sqlalchemy.orm import Session
from admin.database import engine, Base, User
import pymysql
import datetime
import os

import admin.database as db

universitydataDelete = Blueprint('dataDelete', __name__, template_folder=os.path.join(
    os.getcwd(), 'admin\\templates\\Counselling'))


@universitydataDelete.route('/dataDelete', methods = ['GET', 'POST'])
def dataDelete():
    if session.get('logged_in', None):
        msg = ''
        
        if request.method == 'POST':
            name = request.form['name']

            if(db.delete_data(name)):
                msg = "university deleted successfully"
            else:
                msg = "University not exists!"

        try:
            return render_template('dataDelete.html', msg = msg)
        except TemplateNotFound:
            abort(404)
    else:
        return redirect(url_for('login.login'))
