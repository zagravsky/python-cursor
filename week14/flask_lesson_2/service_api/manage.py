from flask_migrate import MigrateCommand
from flask_script import Manager

from service_api import run_app

manager = Manager(run_app())
# manager.add_option("-c", "--config", dest="config_module", required=False)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
