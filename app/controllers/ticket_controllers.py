from flask import render_template, url_for, redirect, flash
from flask_login import current_user
from flask_security import roles_accepted

from app.models import db, Ticket, TicketStatus, User, Group
from app.forms.ticket_forms import CreateTicketForm, UpdateTicketForm


@roles_accepted("admin", "analyst", "manager")
def tickets_list():
    roles = [role.name for role in current_user.roles]
    query = Ticket.query

    if "manager" in roles:
        query = query.filter_by(group_id=current_user.group_id)

    elif "analyst" in roles:
        query = query.filter_by(user_id=current_user.id)

    tickets = query.all()

    return render_template("tickets/tickets_list.html", tickets=tickets)


@roles_accepted("admin")
def tickets_create():
    form = CreateTicketForm()
    if form.validate_on_submit():
        title = form.title.data
        status = TicketStatus[form.status.data]
        note = form.note.data
        group_id = form.group_id.data
        ticket = Ticket(
            title=title,
            status=status,
            note=note,
            group_id=group_id
        )
        db.session.add(ticket)
        db.session.commit()
        flash("Ticket created successfully!", "success")
        return redirect(url_for("tickets_bp.tickets_list"))

    return render_template("tickets/tickets_create.html", form=form)


@roles_accepted("admin", "analyst", "manager")
def tickets_detail(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    return render_template("tickets/tickets_detail.html", ticket=ticket)


@roles_accepted("admin", "analyst", "manager")
def tickets_update(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    form = UpdateTicketForm(obj=ticket)
    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.status = TicketStatus[form.status.data]
        ticket.note = form.note.data
        ticket.users = [User.query.get(user_id) for user_id in form.users.data]

        db.session.commit()
        flash("Ticket updated successfully!", "success")
        return redirect(url_for(
            "tickets_bp.tickets_detail",
            ticket_id=ticket_id
        ))

    form.users.data = [user.id for user in ticket.users]
    roles = [role.name for role in current_user.roles]

    return render_template(
        "tickets/tickets_update.html",
        form=form,
        roles=roles
    )


@roles_accepted("admin")
def tickets_delete(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash("Ticket deleted successfully!", "success")
    return redirect(url_for("tickets_bp.tickets_list"))
