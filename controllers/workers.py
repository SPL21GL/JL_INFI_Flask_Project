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
    '# Shows all workers and pages them.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    page = request.args.get('page', 1, type=int)
    workers = session.query(Mitarbeiter).order_by(Mitarbeiter.MitarbeiterID).paginate(
        page, ROWS_PER_PAGE, error_out=False)

    return render_template("workers.html", paginator=workers)


@workers_blueprint.route("/addWorkersForm", methods=["get", "post"])
def show_add_form():
    '# Shows the form where you can add new workers and also adds them to the database.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_form_object = addWorkersForm()
    if add_form_object.validate_on_submit():
        worker_object = Mitarbeiter()
        worker_object.Voname = add_form_object.Voname.data
        worker_object.Nachname = add_form_object.Nachname.data
        worker_object.Lohn = add_form_object.Lohn.data
        worker_object.Adresse = add_form_object.Adresse.data
        worker_object.Beschäftigung = add_form_object.Beschäftigung.data
        worker_object.Geburtsdatum = add_form_object.Geburtsdatum.data
        worker_object.Arbeitergruppe = add_form_object.Arbeitergruppe.data
        session.add(worker_object)
        session.commit()
        redirect("/")
    return render_template("addWorkers.html",  form=add_form_object)


@workers_blueprint.route("/workers/edit")
def show_edit_form():
    '# Shows the form where you can edit workers.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    worker_id = request.args["worker_id"]
    item_to_edit = session.query(Mitarbeiter).filter(Mitarbeiter.MitarbeiterID == worker_id).first()

    edit_form_object = EditWorkersForm()
    edit_form_object.MitarbeiterId.data = item_to_edit.MitarbeiterID
    edit_form_object.Voname.data = item_to_edit.Voname
    edit_form_object.Nachname.data = item_to_edit.Nachname
    edit_form_object.Lohn.data = item_to_edit.Lohn
    edit_form_object.Adresse.data = item_to_edit.Adresse
    edit_form_object.Beschäftigung.data = item_to_edit.Beschäftigung
    edit_form_object.Geburtsdatum.data = item_to_edit.Geburtsdatum
    return render_template("editWorkers.html", form=edit_form_object)


@workers_blueprint.route("/workers/edit", methods=["get", "post"])
def submit_edit_form():
    '# Updates changes to the workers in the database.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    edit_form_object = EditWorkersForm()
    print(edit_form_object.MitarbeiterId)

    if edit_form_object.validate_on_submit():
        worker_id = edit_form_object.MitarbeiterId.data

        item_to_edit = session.query(Mitarbeiter).filter(
            Mitarbeiter.MitarbeiterID == worker_id).first()
        print(item_to_edit)
        item_to_edit.Voname = edit_form_object.Voname.data
        item_to_edit.Nachname = edit_form_object.Nachname.data
        item_to_edit.Lohn = edit_form_object.Lohn.data
        item_to_edit.Adresse = edit_form_object.Adresse.data
        item_to_edit.Beschäftigung = edit_form_object.Beschäftigung.data
        item_to_edit.Geburtsdatum = edit_form_object.Geburtsdatum.data

        session.commit()

        return redirect("/workers")
    else:
        raise("Fatal Error")


@workers_blueprint.route("/workers/delete", methods=["post"])
def delete_workers():
    '# Deletes worker out of database and then redirects to the overview.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    delete_form_object = DeleteWorkersForm()

    if delete_form_object.validate_on_submit():
        worker_to_delete_id = delete_form_object.MitarbeiterID.data
        worker_to_delete = session.query(Mitarbeiter).filter(
            Mitarbeiter.MitarbeiterID == worker_to_delete_id)
        worker_to_delete.delete()
        session.commit()
    else:
        raise("Fatal Error")
    return redirect("/workers")
