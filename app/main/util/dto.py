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