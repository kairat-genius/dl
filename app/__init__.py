from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')



from app.database import models