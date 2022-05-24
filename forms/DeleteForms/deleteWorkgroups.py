from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteWorkgroupsForm(FlaskForm):
    '# Defines the field of the workgroup to delete.'
    ArbeitsgruppenID = HiddenField("ArbeitsgruppenID")
