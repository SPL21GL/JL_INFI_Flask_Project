from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditCompartmentsForm(FlaskForm):
    AbteilungsId = HiddenField("CompartmentId")
    Name = StringField("Name")
    Gebäude = DecimalField("Building")
