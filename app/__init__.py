from flask import Flask
from config import Config
from .auth.routes import auth
from .feed.routes import feed
from app.models import db
from flask_migrate import Migrate
from .pokemon.routes import pokemon

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(feed)
app.register_blueprint(pokemon)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models