from cloudinary.templatetags import cloudinary
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# mysql account
USERNAME_DB = ''
PASSWORD_DB = ''
NAME_DB = ''
IP_DB = 'localhost'

# cloudinary account
CLOUD_NAME = ''
API_KEY = ''
API_SECRET = ''

# flask config
app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_FLUID_LAYOUT"] = True
app.config["SQLALCHEMY_ECHO"] = True
app.secret_key = b'21137afa59a4dd08b708dcf106c724f9'

# init
db = SQLAlchemy(app=app)
admin = Admin(app=app, name="", template_mode="bootstrap4")
login = LoginManager(app=app)
cloudinary.config(cloud_name=CLOUD_NAME,
                  api_key=API_KEY,
                  api_secret=API_SECRET)


def initTables():
    try:
        db.create_all()
    except:
        db.session.rollback()


def initAdmin():
    pass
