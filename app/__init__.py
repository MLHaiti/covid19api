from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.people_controller import api as people_ns
from .main.controller.communes_controller import api as communes_ns
from .main.controller.departements_controller import api as departements_ns
from .main.controller.mspp_report_age_controller import api as mspp_report_age_ns
from .main.controller.mspp_report_departement_controller import api as mspp_report_departement_ns

blueprint = Blueprint('api', __name__,#url_prefix='/api',
static_url_path='static'
)

static_blueprint = Blueprint('reactjs',__name__,url_prefix='/',
static_url_path='static'
)

api = Api(blueprint,
          title='REST API for MLHAITI covid19',
          version='1.0',
          description='A rest ',
          doc='/'
          )

api.add_namespace(people_ns, path='/api/people')
api.add_namespace(user_ns, path='/api/user')
api.add_namespace(communes_ns, path='/api/communes')
api.add_namespace(departements_ns, path='/api/departements')
api.add_namespace(mspp_report_age_ns, path='/api/mspp/report/age')
api.add_namespace(mspp_report_departement_ns, path='/api/mspp/report/departement')
api.add_namespace(auth_ns)
