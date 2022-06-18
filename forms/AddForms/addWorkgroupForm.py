from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

choices = [("Support", "Support"), ("IT ", "IT "), ("Marketing", "Marketing")]


class AddWorkgroupsForm(FlaskForm):
    '# Defines the fields for add workgroups form.'
    Name = StringField("Name", validators=[validators.Length(
        3, 100), validators.input_required()])
    Raum = DecimalField("Room", validators=[validators.input_required()])
    Abteilung = SelectField("status", choices=choices)
