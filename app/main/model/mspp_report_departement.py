from .. import db, flask_bcrypt
import datetime
from ..config import key
from app.main.model.ht_departments import Departements


class MSPPReportDept(db.Model):
    """ MSSP Report  Model by departement """
    __tablename__ = "mspp_report_departement"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date =db.Column(db.Date, nullable=False)
    ref = db.Column(db.String(255), nullable=True)
    specimen = db.Column(db.Float, nullable=True)
    tested = db.Column(db.Float, nullable=False)
    positive = db.Column(db.Float, nullable=False)
    negative = db.Column(db.Float, nullable=True)
    decease = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String,nullable=True)
    departement_id = db.Column(db.Integer, db.ForeignKey('ht_departements.id_dep'),
        nullable=False)
    ht_departements = db.relationship("Departements")