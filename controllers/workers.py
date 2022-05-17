from flask import Blueprint, redirect, request, render_template
import sqlalchemy
from forms.EditForms.editWorkersForm import EditWorkersForm
from models import db, Mitarbeiter
from forms.AddForms.addWorkersForm import addWorkersForm
from forms.DeleteForms.deleteWorkers import DeleteWorkersForm

ROWS_PER_PAGE = 5
workers_blueprint = Blueprint('workers_blueprint', __name__)


@workers_blueprint.route("/workers", methods=["get", "post"])
def show_workers():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    page = request.args.get('page', 1, type=int)
    workers = session.query(Mitarbeiter).order_by(Mitarbeiter.MitarbeiterID).paginate(
        page, ROWS_PER_PAGE, error_out=False)

    return render_template("workers.html", paginator=workers)


@workers_blueprint.route("/addWorkersForm", methods=["get", "post"])
def showAddForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    addWorkersFormObject = addWorkersForm()
    if addWorkersFormObject.validate_on_submit():
        WorkerObjekt = Mitarbeiter()
        WorkerObjekt.Voname = addWorkersFormObject.Voname.data
        WorkerObjekt.Nachname = addWorkersFormObject.Nachname.data
        WorkerObjekt.Lohn = addWorkersFormObject.Lohn.data
        WorkerObjekt.Adresse = addWorkersFormObject.Adresse.data
        WorkerObjekt.Beschäftigung = addWorkersFormObject.Beschäftigung.data
        WorkerObjekt.Geburtsdatum = addWorkersFormObject.Geburtsdatum.data
        session.add(WorkerObjekt)
        session.commit()
        redirect("/")
    return render_template("addWorkers.html",  form=addWorkersFormObject)


@workers_blueprint.route("/workers/edit")
def showEditForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    worker_id = request.args["worker_id"]
    item_to_edit = session.query(Mitarbeiter).filter(Mitarbeiter.MitarbeiterID == worker_id).first()

    editWorkerFromObject = EditWorkersForm()
    editWorkerFromObject.MitarbeiterId.data = item_to_edit.MitarbeiterID
    editWorkerFromObject.Voname.data = item_to_edit.Voname
    editWorkerFromObject.Nachname.data = item_to_edit.Nachname
    editWorkerFromObject.Lohn.data = item_to_edit.Lohn
    editWorkerFromObject.Adresse.data = item_to_edit.Adresse
    editWorkerFromObject.Beschäftigung.data = item_to_edit.Beschäftigung
    editWorkerFromObject.Geburtsdatum.data = item_to_edit.Geburtsdatum
    return render_template("editWorkers.html", form=editWorkerFromObject)


@workers_blueprint.route("/workers/edit", methods=["get", "post"])
def submitEditForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    editWorkerFromObject = EditWorkersForm()

    if editWorkerFromObject.validate_on_submit():
        worker_id = editWorkerFromObject.MitarbeiterId.data

        item_to_edit = session.query(Mitarbeiter).filter(
            Mitarbeiter.MitarbeiterID == worker_id).first()
        item_to_edit.Voname = editWorkerFromObject.Voname.data
        item_to_edit.Nachname = editWorkerFromObject.Nachname.data
        item_to_edit.Lohn = editWorkerFromObject.Lohn.data
        item_to_edit.Adresse = editWorkerFromObject.Adresse.data
        item_to_edit.Beschäftigung = editWorkerFromObject.Beschäftigung.data
        item_to_edit.Geburtsdatum = editWorkerFromObject.Geburtsdatum.data

        session.commit()

        return redirect("/workers")
    else:
        raise("Fatal Error")


@workers_blueprint.route("/workers/delete", methods=["post"])
def deleteWorkers():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    deleteWorkersFormObject = DeleteWorkersForm()

    if deleteWorkersFormObject.validate_on_submit():
        worker_to_delete_id = deleteWorkersFormObject.MitarbeiterID.data
        worker_to_delete = session.query(Mitarbeiter).filter(
            Mitarbeiter.MitarbeiterID == worker_to_delete_id)
        worker_to_delete.delete()
        session.commit()
    else:
        raise("Fatal Error")
    return redirect("/workers")
