from flask import Flask
from config import Config
from .auth.routes import auth
from .feed.routes import feed
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(feed)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models