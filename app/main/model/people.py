
from .. import db, flask_bcrypt
import datetime
from ..config import key
# from geoalchemy import GeometryColumn, GeometryDDL, Point, Polygon
from geoalchemy2 import Geometry


class People(db.Model):
    """ People Model for storing person related details """
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    symptoms = db.Column(db.String,nullable=False)
    comment = db.Column(db.String,nullable=False)
    geom = db.Column(Geometry("POINT"))
