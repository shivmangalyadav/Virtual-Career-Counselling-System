from flask import Blueprint, Flask, render_template, abort,session,redirect,url_for
from jinja2 import TemplateNotFound

import os

Adminlogout = Blueprint('logout', __name__, template_folder=os.path.join(os.getcwd(), 'admin\\templates\\Auth'))

@Adminlogout.route('/logout')
def logout():
    session.clear()
    try:
        return redirect(url_for('login.login'))
    except TemplateNotFound:
        abort(404)