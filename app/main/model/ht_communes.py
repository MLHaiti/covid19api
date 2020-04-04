
from .. import db, flask_bcrypt
import datetime
from ..config import key
# from geoalchemy import GeometryColumn, GeometryDDL, Point, Polygon
from geoalchemy2 import Geometry


class Communes(db.Model):
    """ People Model for storing person related details """
    __tablename__ = "ht_communes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    geom = db.Column(Geometry(geometry_type='MULTIPOLYGON', srid=4326), autoincrement=False, nullable=True)
    id_dep = db.Column(db.Integer, autoincrement=False, nullable=True)
    departemen = db.Column(db.VARCHAR(length=254), autoincrement=False, nullable=True)
    shape_leng = db.Column(db.NUMERIC(), autoincrement=False, nullable=True)
    id_com = db.Column( db.INTEGER(), autoincrement=False, nullable=True)
    commune = db.Column( db.VARCHAR(length=254), autoincrement=False, nullable=True)
    departemen = db.Column( db.VARCHAR(length=254), autoincrement=False, nullable=True)
    latitude = db.Column( db.NUMERIC(), autoincrement=False, nullable=True)
    longitude = db.Column( db.NUMERIC(), autoincrement=False, nullable=True)

    shape_le_1 = db.Column(db.NUMERIC(), autoincrement=False, nullable=True)
    shape_area = db.Column(db.NUMERIC(), autoincrement=False, nullable=True)