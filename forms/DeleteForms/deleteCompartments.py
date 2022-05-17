from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteCompartmentsForm(FlaskForm):
    AbteilungsID = HiddenField("AbteilungsID")
