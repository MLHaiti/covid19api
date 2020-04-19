from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import MSPPReportDepartementDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.mspp_report_departement_service import save_new_report_departement,get_a_report_departement, get_all_report_departement

api = MSPPReportDepartementDto.api
_mspp_dept_report = MSPPReportDepartementDto.mspp_report_departement


@api.route('/')
class MSPPReportDeptList(Resource):
    @api.doc('list_mspp_report_departement')
    # @admin_token_required
    @api.marshal_list_with(_mspp_dept_report, envelope='data')
    def get(self):
        """List all Departement Reports"""
        return get_all_report_departement()

    @api.expect(_mspp_dept_report, validate=True)
    @api.response(201, 'Person successfully created.')
    @api.doc('create a new Report ')
    def post(self):
        """Creates a new Report """
        data = request.json
        return save_new_report_departement(data=data)


@api.route('/<id>')
@api.param('id', 'The Report identifier')
@api.response(404, 'Report not found.')
class People(Resource):
    @api.doc('get a person')
    @api.marshal_with(_mspp_dept_report)
    def get(self, id):
        """get a Report given its identifier"""
        report_dept = get_a_report_departement(id)
        if not report_dept:
            api.abort(404)
        else:
            return report_dept