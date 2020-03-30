from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.people_controller import api as people_ns
from .main.controller.communes_controller import api as communes_ns

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
          doc='/doc/'
          )

api.add_namespace(people_ns, path='/api/people')
api.add_namespace(user_ns, path='/api/user')
api.add_namespace(communes_ns, path='/api/communes')
api.add_namespace(auth_ns)
