from flask import render_template, request, url_for, redirect

from app import db
from app.models import Ticket


def tickets_list():
    tickets = Ticket.query.all()
    return render_template("tickets/tickets_list.html", tickets=tickets)


def tickets_create():
    if request.method == "POST":
        title = request.form["title"]
        note = request.form["note"]
        ticket = Ticket(title=title, note=note)
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for("tickets_bp.tickets_list"))

    return render_template("tickets/tickets_create.html")
