from sqlalchemy.types import Enum as SQLAlchemyEnum

from app.models import db
from app.models.enums import TicketStatus


class TicketUser(db.Model):
    __tablename__ = "tickets_users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    ticket_id = db.Column("ticket_id", db.Integer, db.ForeignKey("ticket.id"))


class Ticket(db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    status = db.Column(SQLAlchemyEnum(TicketStatus), nullable=False, server_default="PENDING")
    note = db.Column(db.String(255))

    group_id = db.Column(
        db.Integer, db.ForeignKey("group.id"), nullable=False
    )
    group = db.relationship("Group", back_populates="tickets")
