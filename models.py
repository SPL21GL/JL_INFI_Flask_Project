# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Abteilung(db.Model):
    __tablename__ = 'abteilung'

    AbteilungsID = db.Column(db.Integer, primary_key=True, unique=True)
    Name = db.Column(db.String(64), nullable=False)
    Gebäude = db.Column(db.Integer, nullable=False)



class Arbeitsgruppe(db.Model):
    __tablename__ = 'arbeitsgruppe'

    ArbeitsgruppenID = db.Column(db.Integer, primary_key=True, unique=True)
    Name = db.Column(db.String(64), nullable=False)
    Raum = db.Column(db.Integer, nullable=False)
    Abteilung = db.Column(db.String(20))



class ArbeitsgruppeMitarbeiter(db.Model):
    __tablename__ = 'arbeitsgruppe_mitarbeiter'

    Arbeitsgruppe_MitarbeiterID = db.Column(db.Integer, primary_key=True, unique=True)
    ArbeitsgruppenID = db.Column(db.ForeignKey('arbeitsgruppe.ArbeitsgruppenID'), index=True)
    MitarbeiterID = db.Column(db.ForeignKey('mitarbeiter.MitarbeiterID'), index=True)

    arbeitsgruppe = db.relationship('Arbeitsgruppe', primaryjoin='ArbeitsgruppeMitarbeiter.ArbeitsgruppenID == Arbeitsgruppe.ArbeitsgruppenID', backref='arbeitsgruppe_mitarbeiters')
    mitarbeiter = db.relationship('Mitarbeiter', primaryjoin='ArbeitsgruppeMitarbeiter.MitarbeiterID == Mitarbeiter.MitarbeiterID', backref='arbeitsgruppe_mitarbeiters')



class Mitarbeiter(db.Model):
    __tablename__ = 'mitarbeiter'

    MitarbeiterID = db.Column(db.Integer, primary_key=True, unique=True)
    Voname = db.Column(db.String(32), nullable=False)
    Nachname = db.Column(db.String(32))
    Lohn = db.Column(db.Integer, nullable=False)
    Adresse = db.Column(db.String(64))
    Beschäftigung = db.Column(db.String(64))
    Geburtsdatum = db.Column(db.Date)
