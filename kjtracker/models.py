from datetime import datetime
from kjtracker import db


class JewelleryRepair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    item_description = db.Column(db.Text, nullable=False)

    # def __repr__(self):
    #     return
