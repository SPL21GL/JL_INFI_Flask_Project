from flask import Blueprint, redirect, request, render_template
import sqlalchemy
from forms.AddForms.addCompartment import AddCompartmentForm
from forms.DeleteForms.deleteCompartments import DeleteCompartmentsForm
from forms.EditForms.editCompartmentsForm import EditCompartmentsForm
from models import db, Abteilung

ROWS_PER_PAGE = 5
compartments_blueprint = Blueprint('compartments_blueprint', __name__)


@compartments_blueprint.route("/compartments", methods=["get","post"])
def show_compartments():
    session : sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    compartments = session.query(Abteilung).order_by(Abteilung.AbteilungsID).paginate(page, ROWS_PER_PAGE, error_out=False)

    return render_template("compartments.html", paginator = compartments)
@compartments_blueprint.route("/addCompartmentsForm", methods=["get","post"])
def showAddForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
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
def showEditForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session

    compartment_id = request.args["compartment_id"]

    item_to_edit = session.query(Abteilung).filter(Abteilung.AbteilungsID == compartment_id).first()

    editCompartmentsFormObject = EditCompartmentsForm()
    editCompartmentsFormObject.AbteilungsId.data = item_to_edit.AbteilungsID
    editCompartmentsFormObject.Name.data = item_to_edit.Name
    editCompartmentsFormObject.Gebäude.data = item_to_edit.Gebäude

    return render_template("editCompartments.html", form = editCompartmentsFormObject)
@compartments_blueprint.route("/compartments/edit",methods=["get","post"])
def submitEditForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    editCompartmentsFormObject = EditCompartmentsForm()

    if editCompartmentsFormObject.validate_on_submit():
        compartment_id = editCompartmentsFormObject.AbteilungsId.data

        item_to_edit = session.query(Abteilung).filter(Abteilung.AbteilungsID == compartment_id).first()
        item_to_edit.Name = editCompartmentsFormObject.Name.data
        item_to_edit.Gebäude = editCompartmentsFormObject.Gebäude.data

        session.commit()

        return redirect("/compartments")
    else:
        raise("Fatal Error")
@compartments_blueprint.route("/compartments/delete", methods=["post"])
def deleteWorkgroups():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    deleteCompartmentsFormObject = DeleteCompartmentsForm()

    if deleteCompartmentsFormObject.validate_on_submit():
        compartment_to_delete_id = deleteCompartmentsFormObject.AbteilungsID.data
        compartment_to_delete = session.query(Abteilung).filter(Abteilung.AbteilungsID == compartment_to_delete_id)
        compartment_to_delete.delete()
        session.commit()
        
    else:
        raise("Fatal Error")
    
    return redirect("/compartments")