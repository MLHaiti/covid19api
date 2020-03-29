import uuid
import datetime

from app.main import db
from app.main.model.people import People
from flask import jsonify


def save_new_person(data):
    people = People.query.filter_by(phone=data['phone']).first()
    if not people:
        new_person = People(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            lat=data['lat'],
            lon=data['lon'],
            comment=data["comment"],
            symptoms=data["symptoms"],
            dob=data["dob"],
            geom='POINT('+str(data["lon"])+' '+str(data["lat"])+')'

        )
        save_changes(new_person)
        return {"status":"saved"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_people():
    return People.query.all()


def get_a_person(id):
    return People.query.filter_by(id=id).first()




def save_changes(data):
    db.session.add(data)
    db.session.commit()

