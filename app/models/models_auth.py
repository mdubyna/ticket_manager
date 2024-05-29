from flask_security import UserMixin, RoleMixin

from app.models import db


class RoleUser(db.Model):
    """
    Model for managing users roles
    """
    __tablename__ = "roles_users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    role_id = db.Column("role_id", db.Integer, db.ForeignKey("role.id"))


class Role(db.Model, RoleMixin):
    """
    Model for managing roles
    """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return self.description


class User(db.Model, UserMixin):
    """
    Model for managing users
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)

    roles = db.relationship(
        "Role",
        secondary="roles_users",
        backref=db.backref("users", lazy="dynamic")
    )
    tickets = db.relationship(
        "Ticket",
        secondary="tickets_users",
        backref=db.backref("users", lazy="dynamic")
    )
    group_id = db.Column(
        "group_id", db.Integer, db.ForeignKey("group.id")
    )
    group = db.relationship("Group", back_populates="users")

    def __repr__(self):
        return self.email
