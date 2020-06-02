from flask import Blueprint, Flask, render_template, abort, redirect, session, url_for,request
from jinja2 import TemplateNotFound
from sqlalchemy.orm import Session
from admin.database import engine, Base, User
import pymysql
import datetime
import os
import collections


import admin.database as db

universitydataUpload = Blueprint('dataUpload', __name__, template_folder=os.path.join(
    os.getcwd(), 'admin\\templates\\Counselling'))


@universitydataUpload.route('/dataUpload', methods = ['GET', 'POST'])
def dataUpload():
    if session.get('logged_in', None):
        universitytype = []
        states = []
        states = []
        msg = ''

        University_type = db.fetch_univeristy_type()   
        for dt in University_type:
            universitytype.append(dt['UniversityType'])

        state_names = db.fetch_state()
        for st in state_names:
            result = st["State"].find("-")
            if result != -1:
                states.append(st["State"][:result].strip())
            else:
                states.append(st['State'].strip())

        state = list(collections.OrderedDict.fromkeys(states))
        state.sort()
        
        if request.method == 'POST':
            name = request.form['name']
            address = request.form['address']
            state = request.form['state']
            Utype = request.form['Utype']

            # print(name)
            # print(address)
            # print(state)
            # print(Utype)
        
            if (db.submit_university_data(name, address, state, Utype)):
                msg = "University added successfully"
            else:
                msg = "Try Again!"


        try:
            return render_template('dataUpload.html', Utype = universitytype, state = state, msg = msg)
        except TemplateNotFound:
            abort(404)
    else:
        return redirect(url_for('login.login'))
