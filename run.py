import os
from flask import current_app
from app import create_app, db
from app.models import User
from flask_script import Manager, Shell
# from flask_migrate import Migrate, MigrateCommand
# import unittest

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
# migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

# @manager.command
# def test():
#     """Run the unit tests."""
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()