from app.models import db


class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    users = db.relationship("User", back_populates="group")
    tickets = db.relationship("Ticket", back_populates="group")
