from flask import Blueprint,  render_template


#from models import db  verfollständigen

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route("/",methods=["get","post"])


def index():
    #session : sqlalchemy.orm.scoping.scoped_session = db.session
    return render_template("index.html")