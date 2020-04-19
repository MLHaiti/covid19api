from flask_restx import Namespace, fields


class PeopleDto:
    api = Namespace('people', description='People related operations')
    people = api.model('people', {
        'phone': fields.String(required=True, description='People phone number'),
        'first_name': fields.String(required=True, description='Firstname'),
        'last_name': fields.String(required=True, description='Lastname'),
        'dob': fields.Date(required=False, description='Dob'),
        'symptoms': fields.String(required=True, description='Symptoms'),
        'lat': fields.Float(description='GPS location'),
        'lon': fields.Float(description='GPS location')
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class CommunesDto:
    api=Namespace('communes', description='Geojson for communes')

class DepartementsDto:
    api=Namespace('departements', description='Geojson for departements')

class MSPPReportDepartementDto:
    api=Namespace('mspp_report_departement', description='Report by departements')
    mspp_report_departement = api.model('mspp_report_departement',{
    'date':fields.Date(required=True,descripttion="Date of the report"),
    'ref': fields.String(required=True),
    'specimen':fields.Float(required=False),
    'tested': fields.Float(required=True),
    'positive':fields.Float(required=True),
    'negative':fields.Float(required=False),
    'decease':fields.Float(required=True),
    'comment': fields.String(required=False),
    'departement_id': fields.Integer(required=True)
    }
    )

class MSPPReportAgeDto:
    api=Namespace('mspp_report_age', description='Report by age')
    mspp_report_age = api.model('mspp_departement_report',{
    'date':fields.Date(required=True,descripttion="Date of the report"),
    'ref': fields.String(required=True),
    'specimen':fields.Float(required=False),
    'tested': fields.Float(required=True),
    'positive':fields.Float(required=True),
    'negative':fields.Float(required=False),
    'decease':fields.Float(required=True),
    'comment': fields.String(required=False),
    'age_range': fields.Integer(required=True)
    }
    )