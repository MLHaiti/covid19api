import uuid
import datetime

from app.main import db
from app.main.model.mspp_report_departement import MSPPReportDept
from flask import jsonify


def save_new_report_departement(data):
    report = MSPPReportDept.query.filter_by(phone=data['date']).first()
    if not report:
        new_report_departement = MSPPReportDept(
            date=data['date'],
            ref=data['ref'],
            specimen=data['specimen'],
            tested=data['tested'],
            positive=data['positive'],
            comment=data["comment"],
            negative=data["negative"],
            departement_id=data["departement_id"]
        )
        save_changes(new_report_departement)
        return {"status":"saved"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Report already exists. Please Log in.',
        }
        return response_object, 409


def get_all_report_departement():
    return MSPPReportDept.query.all()


def get_a_report_departement(id):
    return MSPPReportDept.query.filter_by(id=id).first()




def save_changes(data):
    db.session.add(data)
    db.session.commit()