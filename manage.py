import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint,static_blueprint
from app.main import create_app, db
from app.main.model import user, blacklist,people,lookup_age_range,mspp_report_age,mspp_report_departement, ht_communes,ht_departments

app = create_app(os.environ.get('MLHAITI_ENV') or 'dev')
print(os.environ.get('MLHAITI_ENV') or 'dev' )

app.register_blueprint(blueprint)
app.register_blueprint(static_blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
