from flask import Blueprint

from app.controllers.user_controllers import (
    users_list,
    users_assign_role
)


users_bp = Blueprint("users_bp", __name__)

users_bp.route("/users", methods=["GET"])(users_list)
users_bp.route(
    "/users/<int:user_id>/role",
    methods=["GET", "POST"]
)(users_assign_role)
