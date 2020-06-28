from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
import uuid 
import os 

'''

Author:Ramful Devesh
Date created: 24/06/2020
Last date updated:

Description: Defines logic for devices stored in the house

e.g Device Name, Device public Id, Device State 

'''
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRETKEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'devices_db.sqlite')

db = SQLAlchemy(app)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(500))
    device_public_id = db.Column(db.String(50), unique=True)
    device_state = db.Column(db.Boolean)

