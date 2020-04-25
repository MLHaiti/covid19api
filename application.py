import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint,static_blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

application = create_app(os.environ.get('MLHAITI_ENV') or 'dev')

print(os.environ.get('MLHAITI_ENV') or 'dev' )

application.register_blueprint(blueprint)
application.register_blueprint(static_blueprint)

application.app_context().push()

if __name__ == '__main__':
    application.debug = True
    application.run()