import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint,static_blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

application = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

application.register_blueprint(blueprint)
application.register_blueprint(static_blueprint)

application.app_context().push()

manager = Manager(application)

migrate = Migrate(application, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    application.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    application.debug = True
    application.run()