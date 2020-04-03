from .. import db, flask_bcrypt
import datetime
from ..config import key
from geoalchemy2 import Geometry


class MSPPReportAge(db.Model):
    """ MSSP report Model by age"""
    __tablename__ = "age_mspp_report"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date =db.Column(db.Date, nullable=False)
    ref = db.Column(db.String(255), nullable=False)
    specimen = db.Column(db.Float, nullable=False)
    tested = db.Column(db.Float, nullable=False)
    positive = db.Column(db.Float, nullable=False)
    negative = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String,nullable=False)
    age_range = db.Column(db.Integer, db.ForeignKey('lookup_age_range.id'),
        nullable=False)