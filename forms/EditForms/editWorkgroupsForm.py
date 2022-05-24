from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditWorkgroupsForm(FlaskForm):
    '# Defines the fields for edit workgroups form.'
    ArbeitsgruppenId = HiddenField("WorkgroupId")
    Name = StringField("Name")
    Raum = DecimalField("Room")
