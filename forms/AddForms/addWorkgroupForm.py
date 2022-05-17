from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField
from wtforms import validators


class AddWorkgroupsForm(FlaskForm):
    Name = StringField("Name", validators=[validators.Length(
        3, 100), validators.input_required()])
    Raum = DecimalField("Room", validators=[validators.input_required()])
