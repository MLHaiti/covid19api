from .. import db, flask_bcrypt
import datetime
from ..config import key


class MSPPReportDept(db.Model):
    """ MSSP Report  Model by departement """
    __tablename__ = "mspp_report_departement"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date =db.Column(db.Date, nullable=False)
    ref = db.Column(db.String(255), nullable=False)
    specimen = db.Column(db.Float, nullable=False)
    tested = db.Column(db.Float, nullable=False)
    positive = db.Column(db.Float, nullable=False)
    negative = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String,nullable=False)
    departement_id = db.Column(db.Integer, db.ForeignKey('ht_departements.id_dep'),
        nullable=False)
    ht_departements = db.relationship("Departements")