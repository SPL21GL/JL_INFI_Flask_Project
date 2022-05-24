from flask import Blueprint, redirect, request, render_template
import sqlalchemy
from forms.AddForms.addCompartment import AddCompartmentForm
from forms.DeleteForms.deleteCompartments import DeleteCompartmentsForm
from forms.EditForms.editCompartmentsForm import EditCompartmentsForm
from models import db, Abteilung

ROWS_PER_PAGE = 5
compartments_blueprint = Blueprint('compartments_blueprint', __name__)


@compartments_blueprint.route("/compartments", methods=["get", "post"])
def show_compartments():
    '# Shows all compartments and also pages them.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    compartments = session.query(Abteilung).order_by(Abteilung.AbteilungsID).paginate(
        page, ROWS_PER_PAGE, error_out=False)

    return render_template("compartments.html", paginator=compartments)


@compartments_blueprint.route("/addCompartmentsForm", methods=["get", "post"])
def show_add_form():
    '# Shows the form where you can add new compartments and also adds them to the database.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_compartment_form_object = AddCompartmentForm()

    if add_compartment_form_object.validate_on_submit():
        compartment_objekt = Abteilung()
        compartment_objekt.Name = add_compartment_form_object.Name.data
        compartment_objekt.Gebäude = add_compartment_form_object.Gebäude.data

        session.add(compartment_objekt)
        session.commit()

        redirect("/")

    return render_template("addCompartment.html",  form=add_compartment_form_object)


@compartments_blueprint.route("/compartments/edit")
def show_edit_form():
    '# Shows the form where you can edit compartments and fills in the information.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    compartment_id = request.args["compartment_id"]

    item_to_edit = session.query(Abteilung).filter(Abteilung.AbteilungsID == compartment_id).first()

    edit_form_object = EditCompartmentsForm()
    edit_form_object.AbteilungsId.data = item_to_edit.AbteilungsID
    edit_form_object.Name.data = item_to_edit.Name
    edit_form_object.Gebäude.data = item_to_edit.Gebäude

    return render_template("editCompartments.html", form=edit_form_object)


@compartments_blueprint.route("/compartments/edit", methods=["get", "post"])
def submit_edit_form():
    '# Updates changes from the editform in the database.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    edit_form_object = EditCompartmentsForm()

    if edit_form_object.validate_on_submit():
        compartment_id = edit_form_object.AbteilungsId.data

        item_to_edit = session.query(Abteilung).filter(
            Abteilung.AbteilungsID == compartment_id).first()
        item_to_edit.Name = edit_form_object.Name.data
        item_to_edit.Gebäude = edit_form_object.Gebäude.data

        session.commit()

        return redirect("/compartments")


@compartments_blueprint.route("/compartments/delete", methods=["post"])
def delete_compartments():
    '# Deletes a compartment by ID and then redirects to the overview.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    delete_form_object = DeleteCompartmentsForm()

    if delete_form_object.validate_on_submit():
        compartment_to_delete_id = delete_form_object.AbteilungsID.data
        compartment_to_delete = session.query(Abteilung).filter(
            Abteilung.AbteilungsID == compartment_to_delete_id)
        compartment_to_delete.delete()
        session.commit()
    else:
        raise("Fatal Error")
    return redirect("/compartments")
