from flask import Blueprint

from app.controllers.ticket_controllers import tickets_list, tickets_create


tickets_bp = Blueprint("tickets_bp", __name__)

tickets_bp.route("/tickets", methods=["GET"])(tickets_list)
tickets_bp.route("/tickets/create", methods=["GET", "POST"])(tickets_create)

