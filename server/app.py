from flask import Flask

from admin import Admin
from api.courses import channelmod

app = Flask(__name__, template_folder="admin/templates")
app.config['SECRET_KEY'] = 'hdfhik snak hnahndlkndg dfigjod fsadfd;dsf'

app.register_blueprint(Admin, url_prefix="/admin")
app.register_blueprint(channelmod, url_prefix='/channel')


if __name__ == "__main__":
    app.run(debug=True)
