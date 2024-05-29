from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    widgets,
    SelectMultipleField
)
from wtforms.validators import DataRequired, Length


class GroupForm(FlaskForm):
    """
    Form for creating and updating group and validating data
    """
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=1, max=80)]
    )
    users = SelectMultipleField(
        "Users",
        coerce=int,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
    )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        users = kwargs["users"]
        super(GroupForm, self).__init__(*args, **kwargs)
        self.users.choices = [
            (user.id, user.email)
            for user in users
        ]
