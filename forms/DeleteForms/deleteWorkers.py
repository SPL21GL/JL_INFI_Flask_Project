from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteWorkersForm(FlaskForm):
    MitarbeiterID = HiddenField("MitarbeiterID")
