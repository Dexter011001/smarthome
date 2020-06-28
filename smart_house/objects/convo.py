from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
import uuid 
import os 

'''

Author:Ramful Devesh
Date created: 24/06/2020
Last date updated:

Description: Defines logic for responses if the intent is conversation type

e.g Convo Name (Greeting, SmallTalk), Convo_public_id

'''

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRETKEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'convo_db.sqlite')

db = SQLAlchemy(app)

class Conversation(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    convo_name = db.Column(db.String(100))
    convo_public_id = public_id = db.Column(db.String(50), unique=True)