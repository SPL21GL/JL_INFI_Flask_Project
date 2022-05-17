from flask import Blueprint, redirect, request, render_template
import sqlalchemy
from forms.AddForms.addWorkgroupForm import AddWorkgroupsForm
from forms.EditForms.editWorkgroupsForm import EditWorkgroupsForm
from forms.DeleteForms.deleteWorkgroups import DeleteWorkgroupsForm
from models import Arbeitsgruppe, db

ROWS_PER_PAGE = 5
workgroups_blueprint = Blueprint('workgroups_blueprint', __name__)


@workgroups_blueprint.route("/workgroups", methods=["get", "post"])
def show_workgroups():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    page = request.args.get('page', 1, type=int)
    workgroups = session.query(Arbeitsgruppe).order_by(
        Arbeitsgruppe.ArbeitsgruppenID).paginate(page, ROWS_PER_PAGE, error_out=False)
    return render_template("workgroups.html", paginator=workgroups)


@workgroups_blueprint.route("/addWorkgroupsForm", methods=["get", "post"])
def showAddForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    addWorkgroupFormObject = AddWorkgroupsForm()

    if addWorkgroupFormObject.validate_on_submit():

        WorkgroupObjekt = Arbeitsgruppe()
        WorkgroupObjekt.Name = addWorkgroupFormObject.Name.data
        WorkgroupObjekt.Raum = addWorkgroupFormObject.Raum.data

        session.add(WorkgroupObjekt)
        session.commit()

        redirect("/")

    return render_template("addWorkgroups.html",  form=addWorkgroupFormObject)


@workgroups_blueprint.route("/workgroups/edit")
def showEditForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    workgroup_id = request.args["workgroup_id"]

    item_to_edit = session.query(Arbeitsgruppe).filter(
        Arbeitsgruppe.ArbeitsgruppenID == workgroup_id).first()

    editWorkgroupFromObject = EditWorkgroupsForm()
    editWorkgroupFromObject.ArbeitsgruppenId.data = item_to_edit.ArbeitsgruppenID
    editWorkgroupFromObject.Name.data = item_to_edit.Name
    editWorkgroupFromObject.Raum.data = item_to_edit.Raum

    return render_template("editWorkgroups.html", form=editWorkgroupFromObject)


@workgroups_blueprint.route("/workgroups/edit", methods=["get", "post"])
def submitEditForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    EditWorkgroupsFormObject = EditWorkgroupsForm()

    if EditWorkgroupsFormObject.validate_on_submit():

        workgroup_id = EditWorkgroupsFormObject.ArbeitsgruppenId.data

        item_to_edit = session.query(Arbeitsgruppe).filter(
            Arbeitsgruppe.ArbeitsgruppenID == workgroup_id).first()
        item_to_edit.Name = EditWorkgroupsFormObject.Name.data
        item_to_edit.Raum = EditWorkgroupsFormObject.Raum.data

        session.commit()

        return redirect("/workgroups")
    else:
        raise("Fatal Error")


@workgroups_blueprint.route("/workgroups/delete", methods=["post"])
def deleteWorkgroups():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    deleteWorkgroupsFormObject = DeleteWorkgroupsForm()

    if deleteWorkgroupsFormObject.validate_on_submit():
        workgroup_to_delete_id = deleteWorkgroupsFormObject.ArbeitsgruppenID.data
        print(workgroup_to_delete_id)
        workgroup_to_delete = session.query(Arbeitsgruppe).filter(
            Arbeitsgruppe.ArbeitsgruppenID == workgroup_to_delete_id)
        workgroup_to_delete.delete()
        session.commit()
    else:
        raise("Fatal Error")
    return redirect("/workgroups")
