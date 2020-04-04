from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import MSPPReportAgeDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.mspp_report_age_service import save_new_report_age,get_a_report_age, get_all_report_age

api = MSPPReportAgeDto.api
_mspp_age_report = MSPPReportAgeDto.mspp_report_age


@api.route('/')
class MSPPReportAgeList(Resource):
    @api.doc('list_mspp_report_age')
    # @admin_token_required
    @api.marshal_list_with(_mspp_age_report, envelope='data')
    def get(self):
        """List all People"""
        return get_all_report_age()

    @api.expect(_mspp_age_report, validate=True)
    @api.response(201, 'Person successfully created.')
    @api.doc('create a new Person ')
    def post(self):
        """Creates a new Person """
        data = request.json
        return save_new_report_age(data=data)


@api.route('/<id>')
@api.param('id', 'The Person identifier')
@api.response(404, 'Person not found.')
class People(Resource):
    @api.doc('get a person')
    @api.marshal_with(_mspp_age_report)
    def get(self, id):
        """get a user given its identifier"""
        report_age = get_a_report_age(id)
        if not report_age:
            api.abort(404)
        else:
            return report_age