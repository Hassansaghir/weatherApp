from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class weather(db.Model):
    __tablename__='weather'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text)
    icon=db.Column(db.String(100))
    