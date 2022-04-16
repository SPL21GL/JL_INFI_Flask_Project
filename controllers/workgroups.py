from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from forms.AddForms.addWorkgroupForm import AddWorkgroupsForm
from models import Arbeitsgruppe, db

ROWS_PER_PAGE = 5
workgroups_blueprint = Blueprint('workgroups_blueprint', __name__)


@workgroups_blueprint.route("/workgroups", methods=["get","post"])
def show_workgroups():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    page = request.args.get('page', 1, type=int)
    workgroups = session.query(Arbeitsgruppe).order_by(Arbeitsgruppe.ArbeitsgruppenID).paginate(page, ROWS_PER_PAGE, error_out=False)
    return render_template("workgroups.html", paginator = workgroups)

@workgroups_blueprint.route("/addWorkgroupsForm", methods=["get","post"])
def showAddForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    addWorkgroupFormObject = AddWorkgroupsForm()
    print("0")

    if addWorkgroupFormObject.validate_on_submit():
        print("1")
        
        WorkgroupObjekt = Arbeitsgruppe()
        WorkgroupObjekt.Name = addWorkgroupFormObject.Name.data
        WorkgroupObjekt.Raum = addWorkgroupFormObject.Raum.data

        session.add(WorkgroupObjekt)
        session.commit()

        redirect("/")

    return render_template("addWorkgroups.html",  form=addWorkgroupFormObject)