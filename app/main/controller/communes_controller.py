
from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..service.commune_service import get_all_communes_geojson
from ..util.dto import CommunesDto

api = CommunesDto.api
# _person = PeopleDto.people


@api.route('/geojson')
class  CommuneGeoJSON(Resource):
    @api.doc('list_of_people')
    # @admin_token_required
    #@api.marshal_list_with(_person, envelope='data')
    def get(self):
        """Commune GeoJSON"""
        return get_all_communes_geojson()