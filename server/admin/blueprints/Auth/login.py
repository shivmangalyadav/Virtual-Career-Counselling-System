from flask import Blueprint, Flask, render_template, abort
from jinja2 import TemplateNotFound
from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
from admin.database import engine, Base, User
import os


Adminlogin = Blueprint('login', __name__, template_folder=os.path.join(os.getcwd(), 'admin\\templates\\Auth'))

@Adminlogin.route('/login', methods = ['GET', 'POST'])
def login():
    if session.get('logged_in', None):
        return redirect(url_for('dataUpload.dataUpload'))

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
            return redirect(url_for('dataUpload.dataUpload'))

    return render_template('login.html')
    