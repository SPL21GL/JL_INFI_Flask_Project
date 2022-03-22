from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField, HiddenField,DecimalField

class EditWorkgroupsForm(FlaskForm):
    ArbeitsgruppenId = HiddenField("WorkgroupId")
    Name = StringField("Name")
    Raum = DecimalField("Room")