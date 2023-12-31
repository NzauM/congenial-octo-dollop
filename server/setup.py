import os
from flask import Flask
from flask_migrate import Migrate
# from models import db, Book, Author
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# from app import app,db




app = Flask(__name__,static_url_path='',static_folder='../client/dist', template_folder='../client/dist')

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
print()

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'