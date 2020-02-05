from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, TIMESTAMP

db = SQLAlchemy()


class ChargeNetwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    unit_value = db.Column(db.Float)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
