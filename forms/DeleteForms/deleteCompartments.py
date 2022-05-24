from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteCompartmentsForm(FlaskForm):
    '# Defines the field of the compartment to delete.'
    AbteilungsID = HiddenField("AbteilungsID")
