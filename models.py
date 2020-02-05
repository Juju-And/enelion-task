from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

# ChargeNetwork posiada atrybuty:
#
#     lokalizacja (lat, lng)
#     identyfikator zasobu
#     timestampy utworzenia, modyfikacji
#     kwota jednostkowa za 1kWh


class ChargeNetwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    unit_value = db.Column(db.Float)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow)

