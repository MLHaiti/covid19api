from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import PeopleDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.person_service import get_all_people,get_a_person, save_new_person

api = PeopleDto.api
_person = PeopleDto.people


@api.route('/')
class PeopleList(Resource):
    @api.doc('list_of_people')
    # @admin_token_required
    @api.marshal_list_with(_person, envelope='data')
    def get(self):
        """List all People"""
        return get_all_people()

    @api.expect(_person, validate=True)
    @api.response(201, 'Person successfully created.')
    @api.doc('create a new Person ')
    def post(self):
        """Creates a new Person """
        data = request.json
        return save_new_person(data=data)


@api.route('/<id>')
@api.param('id', 'The Person identifier')
@api.response(404, 'Person not found.')
class People(Resource):
    @api.doc('get a person')
    @api.marshal_with(_person)
    def get(self, public_id):
        """get a user given its identifier"""
        person = get_a_person(id)
        if not person:
            api.abort(404)
        else:
            return person