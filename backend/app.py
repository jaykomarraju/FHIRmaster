from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from firebase_admin import credentials, firestore, initialize_app
from werkzeug.exceptions import BadRequest
import json

# Initialize Firebase
cred = credentials.Certificate('credentials.json')
default_app = initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def post(self):
        # Get the username and password from the request body
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # Check if the username and password are valid
        if username == "admin" and password == "password":
            return {"message": "Login successful."}, 200
        else:
            return {"message": "Invalid credentials."}, 401

class Patient(Resource):
    def get(self, patient_id):
        # Get the patient data for the given ID
        doc_ref = db.collection('patients').document(patient_id)
        doc = doc_ref.get()

        if doc.exists:
            return doc.to_dict(), 200
        else:
            return {"message": "Patient not found."}, 404

    def put(self, patient_id):
        # Get the patient data for the given ID
        doc_ref = db.collection('patients').document(patient_id)
        doc = doc_ref.get()

        if doc.exists:
            # Update the patient data with the new values from the request body
            data = request.get_json()
            doc_ref.update(data)
            return {"message": "Patient data updated.", "data": doc_ref.get().to_dict()}, 200
        else:
            return {"message": "Patient not found."}, 404

class PatientList(Resource):
    def get(self):
        # Return a list of all patients
        patients = []
        docs = db.collection('patients').get()

        for doc in docs:
            patients.append(doc.to_dict())

        return patients, 200

    def post(self):
        # Parse the request body to get the patient data
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("age", type=int, required=True)
        parser.add_argument("gender", type=str, required=True)
        args = parser.parse_args()

        # Generate a new ID for the patient
        doc_ref = db.collection('patients').document()
        patient_id = doc_ref.id

        # Create a new patient object with the given data
        patient = {
            "name": args["name"],
            "age": args["age"],
            "gender": args["gender"]
        }

        # Add the new patient to the database
        doc_ref.set(patient)

        # Return the ID of the new patient
        return {"message": "Patient created.", "id": patient_id}, 201

# Add the resource routes to the API
api.add_resource(Login, "/login")
api.add_resource(Patient, "/patient/<string:patient_id>")
api.add_resource(PatientList, "/patient")

if __name__ == '__main__':
    app.run(debug=True)
