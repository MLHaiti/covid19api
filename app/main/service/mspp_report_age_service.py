import uuid
import datetime

from app.main import db
from app.main.model.mspp_report_age import MSPPReportAge
from flask import jsonify


def save_new_report_age(data):
    report = MSPPReportAge.query.filter_by(phone=data['date']).first()
    if not report:
        new_person = MSPPReportAge(
            date=data['date'],
            ref=data['ref'],
            specimen=data['specimen'],
            tested=data['tested'],
            positive=data['positive'],
            comment=data["comment"],
            negative=data["negative"],
            age_range=data["age_range"]
        )
        save_changes(new_person)
        return {"status":"saved"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Report already exists. Please Log in.',
        }
        return response_object, 409


def get_all_report_age():
    return MSPPReportAge.query.all()


def get_a_report_age(id):
    return MSPPReportAge.query.filter_by(id=id).first()




def save_changes(data):
    db.session.add(data)
    db.session.commit()