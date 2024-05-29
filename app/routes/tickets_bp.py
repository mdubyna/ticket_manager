from flask import Blueprint

from app.controllers.ticket_controllers import (
    tickets_list,
    tickets_create,
    tickets_detail,
    tickets_update,
    tickets_delete
)


tickets_bp = Blueprint("tickets_bp", __name__)

tickets_bp.route("/tickets", methods=["GET"])(tickets_list)
tickets_bp.route("/tickets/create", methods=["GET", "POST"])(tickets_create)
tickets_bp.route("/tickets/<int:ticket_id>", methods=["GET"])(tickets_detail)
tickets_bp.route(
    "/tickets/<int:ticket_id>/update",
    methods=["GET", "POST"]
)(tickets_update)
tickets_bp.route(
    "/tickets/<int:ticket_id>/delete",
    methods=["POST"]
)(tickets_delete)
