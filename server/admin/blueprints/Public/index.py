from flask import Blueprint, Flask, render_template, abort
from jinja2 import TemplateNotFound

import os

Adminindex = Blueprint('index', __name__, template_folder=os.path.join(os.getcwd(), 'admin\\templates\\Public'))


@Adminindex.route('/index')
@Adminindex.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)