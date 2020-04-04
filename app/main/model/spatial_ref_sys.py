
from .. import db, flask_bcrypt
import datetime
from ..config import key
from geoalchemy2 import Geometry


class SpatialRefSys(db.Model):
    """ People Model for storing person related details """
    __tablename__ = "spatial_ref_sys"

    srid = db.Column( db.Integer, primary_key=True, autoincrement=False, nullable=False)
    auth_name = db.Column( db.VARCHAR(length=256), autoincrement=False, nullable=True)
    auth_srid = db.Column( db.Integer, autoincrement=False, nullable=True)
    srtext = db.Column( db.VARCHAR(length=2048), autoincrement=False, nullable=True)
    proj4text = db.Column( db.VARCHAR(length=2048), autoincrement=False, nullable=True)