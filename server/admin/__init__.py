from flask import Blueprint, Flask, render_template, abort
from jinja2 import TemplateNotFound
from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
from database import engine, Base, User
import os
import collections

from database import AdminUniversity

university = AdminUniversity()

Admin = Blueprint('admin', __name__, template_folder=os.path.join(os.getcwd(), 'admin'))

@Admin.route('/login', methods = ['GET', 'POST'])
def login():
    if session.get('logged_in', None):
        return redirect(url_for('admin.dataUpload'))

    if request.method == 'POST':
        email = request.form['txtEmail']
        psw = request.form['txtPwd']
        ssn = Session(engine)

        f = Fernet('ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=')

        data = ssn.query(User).filter_by(AdminEmail = email).first()
        
        if data:
            # print(f.decrypt(data.AdminPassword.encode()).decode())
            # print(psw)
            if psw == f.decrypt(data.AdminPassword.encode()).decode():
                status = True
                session['logged_in'] = True
                session['Adminname'] = data.AdminName
                session['AdminEmail'] = data.AdminEmail
                
            else:
                status = False
        else:
            status = False
        ssn.close()

        if not status:
            return render_template('login.html',msg = 'Login failed')
        else:
            return redirect(url_for('admin.dataUpload'))

    return render_template('login.html')



@Admin.route('/logout')
def logout():
    session.clear()
    try:
        return redirect(url_for('admin.login'))
    except TemplateNotFound:
        abort(404)




@Admin.route('/dataDelete', methods = ['GET', 'POST'])
def dataDelete():
    if session.get('logged_in', None):
        msg = ''
        
        if request.method == 'POST':
            name = request.form['name']

            if(university.delete_data(name)):
                msg = "university deleted successfully"
            else:
                msg = "University not exists!"

        try:
            return render_template('dataDelete.html', msg = msg)
        except TemplateNotFound:
            abort(404)
    else:
        return redirect(url_for('admin.login'))




@Admin.route('/dataUpload', methods = ['GET', 'POST'])
def dataUpload():
    if session.get('logged_in', None):
        universitytype = []
        states = []
        states = []
        msg = ''

        University_type = university.fetch_univeristy_type()   
        for dt in University_type:
            universitytype.append(dt['UniversityType'])

        state_names = university.fetch_state()
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
        
            if (university.submit_university_data(name, address, state, Utype)):
                msg = "University added successfully"
            else:
                msg = "Try Again!"


        try:
            return render_template('dataUpload.html', Utype = universitytype, state = state, msg = msg)
        except TemplateNotFound:
            abort(404)
    else:
        return redirect(url_for('admin.login'))


@Admin.route('/index')
@Admin.route('/')
def Home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)