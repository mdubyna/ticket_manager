from flask import render_template, redirect, url_for, request, flash
from flask_security import current_user, roles_required
from app.models import db, User, Role
from app.forms.user_forms import UserRolesForm


@roles_required("admin")
def users_list():
    users = User.query.all()
    return render_template("users/users_list.html", users=users)


@roles_required("admin")
def users_assign_role(user_id):
    user = User.query.get_or_404(user_id)
    form = UserRolesForm(obj=user)

    if form.validate_on_submit():
        user.roles = [Role.query.get(role_id) for role_id in form.roles.data]
        db.session.commit()
        flash("Roles updated successfully.", "success")
        return redirect(url_for("users_bp.users_list"))

    form.roles.data = [role.id for role in user.roles]
    return render_template("users/users_roles.html", user=user, form=form)
