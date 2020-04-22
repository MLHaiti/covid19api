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
        """List all report by age"""
        return get_all_report_age()

    @api.expect(_mspp_age_report, validate=True)
    @api.response(201, 'Age\'s report successfully created.')
    @api.doc('create a new age report ')
    def post(self):
        """Creates a new age report """
        data = request.json
        return save_new_report_age(data=data)


@api.route('/<id>')
@api.param('id', 'The report identifier')
@api.response(404, 'report not found.')
class People(Resource):
    @api.doc('get an age report')
    @api.marshal_with(_mspp_age_report)
    def get(self, id):
        """get an age report given its identifier"""
        report_age = get_a_report_age(id)
        if not report_age:
            api.abort(404)
        else:
            return report_age