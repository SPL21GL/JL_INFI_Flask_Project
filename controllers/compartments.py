from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from forms.AddForms.addCompartment import AddCompartmentForm
from models import db, Abteilung


compartments_blueprint = Blueprint('compartments_blueprint', __name__)


@compartments_blueprint.route("/compartments", methods=["get","post"])
def compartment():
    session : sqlalchemy.orm.scoping.scoped_session = db.session



    compartments = session.query(Abteilung).all()
    return render_template("compartments.html", compartments = compartments)
@compartments_blueprint.route("/addCompartmentsForm", methods=["get","post"])
def showAddForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    addCompartmentFormObject = AddCompartmentForm()

    if addCompartmentFormObject.validate_on_submit():
        
        CompartmentObjekt = Abteilung()
        CompartmentObjekt.Name = addCompartmentFormObject.Name.data
        CompartmentObjekt.Gebäude = addCompartmentFormObject.Gebäude.data

        session.add(CompartmentObjekt)
        session.commit()

        redirect("/")

    return render_template("addCompartment.html",  form=addCompartmentFormObject)