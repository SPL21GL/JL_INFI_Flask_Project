from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField

class DeleteWorkgroupsForm(FlaskForm):
    ArbeitsgruppenID = HiddenField("ArbeitsgruppenID")