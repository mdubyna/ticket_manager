from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, widgets
from app.models import Role


class UserRolesForm(FlaskForm):
    """
    Form for managing user roles
    """
    roles = SelectMultipleField("Roles",
                                coerce=int,
                                option_widget=widgets.CheckboxInput(),
                                widget=widgets.ListWidget(prefix_label=False))
    submit = SubmitField("Assign Roles")

    def __init__(self, *args, **kwargs):
        super(UserRolesForm, self).__init__(*args, **kwargs)
        self.roles.choices = [
            (role.id, role.name)
            for role in Role.query.all()
        ]
