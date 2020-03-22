
from .. import db, flask_bcrypt
import datetime
from ..config import key
import jwt


class People(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "covid19ht_people"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), unique=True, nullable=False)
    last_name = db.Column(db.String(255), unique=True, nullable=False)
    gps = db.Column(db.String(255), unique=True, nullable=False)
