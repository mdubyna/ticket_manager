from flask import render_template, url_for, redirect, flash
from flask_security import roles_accepted
from sqlalchemy import or_

from app.models import db, User, Group
from app.forms.group_forms import GroupForm


@roles_accepted("admin", "analyst", "manager")
def groups_list():
    groups = Group.query.all()
    return render_template("groups/groups_list.html", groups=groups)


@roles_accepted("admin")
def groups_create():
    users = User.query.filter_by(group_id=None).all()
    form = GroupForm(users=users)
    if form.validate_on_submit():
        name = form.name.data
        users = [User.query.get(user_id) for user_id in form.users.data]
        group = Group(
            name=name,
            users=users
        )
        db.session.add(group)
        db.session.commit()
        flash("Group created successfully!", "success")
        return redirect(url_for("groups_bp.groups_list"))

    return render_template("groups/groups_create.html", form=form)


@roles_accepted("admin", "analyst", "manager")
def groups_detail(group_id):
    group = Group.query.get_or_404(group_id)
    return render_template("groups/groups_detail.html", group=group)


@roles_accepted("admin")
def groups_update(group_id):
    group = Group.query.get_or_404(group_id)
    users = User.query.filter(or_(User.group_id == group_id, User.group_id == None)).all()
    form = GroupForm(obj=group, users=users)
    if form.validate_on_submit():
        group.name = form.name.data
        group.users = [User.query.get(user_id) for user_id in form.users.data]

        db.session.commit()
        flash("Group updated successfully!", "success")
        return redirect(url_for("groups_bp.groups_detail", group_id=group_id))

    form.users.data = [user.id for user in group.users]

    return render_template("groups/groups_update.html", form=form)


@roles_accepted("admin")
def groups_delete(group_id):
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    flash("Group deleted successfully!", "success")
    return redirect(url_for("groups_bp.groups_list"))
