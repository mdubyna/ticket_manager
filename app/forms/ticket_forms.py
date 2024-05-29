from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    SelectMultipleField,
    widgets
)
from wtforms.validators import DataRequired, Length

from app.models import TicketStatus, Group, User


class TicketForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=80)])
    status = SelectField(
        "Status",
        choices=[(tag.name, tag.value) for tag in TicketStatus],
        validators=[DataRequired()]
    )
    note = StringField("Note", validators=[Length(max=255)])

    submit = SubmitField("Submit")


class CreateTicketForm(TicketForm):
    group_id = SelectField("Group", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.group_id.choices = [(group.id, group.name) for group in Group.query.all()]


class UpdateTicketForm(TicketForm):
    users = SelectMultipleField(
        "Users",
        coerce=int,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
    )

    def __init__(self, *args, **kwargs):
        group_users = User.query.filter_by(group_id=kwargs["obj"].group_id).all()
        super(TicketForm, self).__init__(*args, **kwargs)
        self.users.choices = [
            (user.id, user.email)
            for user in group_users
        ]
