from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.from_pyfile('settings.py')


redis_client = FlaskRedis(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')



from app.database import models