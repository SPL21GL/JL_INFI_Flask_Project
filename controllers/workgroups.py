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
    '# Shows all workgroups and pages them.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    page = request.args.get('page', 1, type=int)
    workgroups = session.query(Arbeitsgruppe).order_by(
        Arbeitsgruppe.ArbeitsgruppenID).paginate(page, ROWS_PER_PAGE, error_out=False)
    return render_template("workgroups.html", paginator=workgroups)


@workgroups_blueprint.route("/addWorkgroupsForm", methods=["get", "post"])
def show_add_form():
    '# Shows the form where you can add workers.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_form_object = AddWorkgroupsForm()

    if add_form_object.validate_on_submit():

        workgroup_object = Arbeitsgruppe()
        workgroup_object.Name = add_form_object.Name.data
        workgroup_object.Raum = add_form_object.Raum.data
        workgroup_object.Abteilung = request.form.get("Abteilung")
        print(workgroup_object.Abteilung)

        session.add(workgroup_object)
        session.commit()

        redirect("/")

    return render_template("addWorkgroups.html",  form=add_form_object)


@workgroups_blueprint.route("/workgroups/edit")
def show_edit_form():
    '# Shows the form where you can edit workgroups.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    workgroup_id = request.args["workgroup_id"]

    item_to_edit = session.query(Arbeitsgruppe).filter(
        Arbeitsgruppe.ArbeitsgruppenID == workgroup_id).first()

    edit_form_object = EditWorkgroupsForm()
    edit_form_object.ArbeitsgruppenId.data = item_to_edit.ArbeitsgruppenID
    edit_form_object.Name.data = item_to_edit.Name
    edit_form_object.Raum.data = item_to_edit.Raum
    edit_form_object.Abteilung.data = item_to_edit.Abteilung
    default = item_to_edit.Abteilung
    return render_template("editWorkgroups.html", form=edit_form_object, default=default)


@workgroups_blueprint.route("/workgroups/edit", methods=["get", "post"])
def submit_edit_form():
    '# Updates changes to the workgroups in the database.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    edit_form_object = EditWorkgroupsForm()

    if edit_form_object.validate_on_submit():

        workgroup_id = edit_form_object.ArbeitsgruppenId.data

        item_to_edit = session.query(Arbeitsgruppe).filter(
            Arbeitsgruppe.ArbeitsgruppenID == workgroup_id).first()
        item_to_edit.Name = edit_form_object.Name.data
        item_to_edit.Raum = edit_form_object.Raum.data
        item_to_edit.Abteilung = edit_form_object.Abteilung.data

        session.commit()

        return redirect("/workgroups")
    else:
        raise("Fatal Error")


@workgroups_blueprint.route("/workgroups/delete", methods=["post"])
def delete_workgroups():
    '# Deletes workgroups out of database and then redirects to the overview.'
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    delete_form_object = DeleteWorkgroupsForm()

    if delete_form_object.validate_on_submit():
        workgroup_to_delete_id = delete_form_object.ArbeitsgruppenID.data
        print(workgroup_to_delete_id)
        workgroup_to_delete = session.query(Arbeitsgruppe).filter(
            Arbeitsgruppe.ArbeitsgruppenID == workgroup_to_delete_id)
        workgroup_to_delete.delete()
        session.commit()
    return redirect("/workgroups")
