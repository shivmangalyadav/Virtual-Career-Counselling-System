from flask import Flask
from flask_jwt_extended import JWTManager

from admin import Admin
from api.courses import channelmod
from api.users import User

app = Flask(__name__, template_folder="admin/templates")
app.config['SECRET_KEY'] = 'hdfhik snak hnahndlkndg dfigjod fsadfd;dsf'

app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)

app.register_blueprint(Admin, url_prefix="/admin")
app.register_blueprint(channelmod, url_prefix='/channel')
app.register_blueprint(User, url_prefix='/user')


if __name__ == "__main__":
    app.run(debug=True)
