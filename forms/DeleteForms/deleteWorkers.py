from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteWorkersForm(FlaskForm):
    '# Defines the field of the worker to delete.'
    MitarbeiterID = HiddenField("MitarbeiterID")
