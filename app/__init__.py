from flask import Flask
from config import DevConfig,ProdConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(ProdConfig)
db.init_app(app)

# from app.fmu import bp as fmu_bp
# app.register_blueprint(api_bp, url_prefix='/api')


from app import models,routes