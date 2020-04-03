from .. import db, flask_bcrypt
import datetime
from ..config import key
from geoalchemy2 import Geometry


class AgeRange(db.Model):
    """ Age range for report """
    __tablename__ = "lookup_age_range"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.String,nullable=False)