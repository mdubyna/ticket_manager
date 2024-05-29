from flask import Blueprint

from app.controllers.group_controllers import (
    groups_list,
    groups_create,
    groups_detail,
    groups_update,
    groups_delete
)


groups_bp = Blueprint("groups_bp", __name__)

groups_bp.route("/groups", methods=["GET"])(groups_list)
groups_bp.route("/groups/create", methods=["GET", "POST"])(groups_create)
groups_bp.route("/groups/<int:group_id>", methods=["GET"])(groups_detail)
groups_bp.route(
    "/groups/<int:group_id>/update",
    methods=["GET", "POST"]
)(groups_update)
groups_bp.route(
    "/groups/<int:group_id>/delete",
    methods=["POST"]
)(groups_delete)
