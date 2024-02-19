# Import necessary Flask extensions and utility functions.
from flask_restful import Resource, reqparse, request
from flask import jsonify
from .swen_610_db_utils import *  
from .ritinfo import * 
import json

# Define an InfoItem class that represents an entity containing user details.
class InfoItem:
    # Constructor to initialize an InfoItem object with necessary attributes.
    def __init__(self, firstname, lastname, email, uid, mobilenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.uid = uid
        self.mobilenumber = mobilenumber

    # Accept method that allows a visitor to perform operations on the InfoItem instance.
    # This method is part of the Visitor pattern and allows for extending functionality without modifying the class.
    def accept(self, visitor):
        return visitor.visit_info_item(self)

# Abstract base class for visitors that perform operations on InfoItem instances.
class InfoItemVisitor:
    def visit_info_item(self, info_item):
        # Placeholder method to be overridden by concrete visitor implementations.
        raise NotImplementedError

# Concrete visitor class for validating InfoItem instances.
class InfoItemValidator(InfoItemVisitor):
    def visit_info_item(self, info_item):
        # Perform validation checks on the InfoItem instance.
        errors = []
        if '@' not in info_item.email:
            errors.append('Invalid email address')
        # Return a list of any found errors.
        return errors

# Resource class for handling CRUD operations on info items via RESTful APIs.
class InfoDetails(Resource):
    # Handle GET requests to fetch all info items.
    def get(self):
        # Utilize a utility function to fetch and return all info items as JSON.
        return jsonify(list_info_items())

    # Handle POST requests to create a new info item.
    def post(self):
        # Parse incoming JSON data from the request.
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=str, required=True, location='json')
        parser.add_argument('lastname', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('uid', type=str, required=True, location='json')
        parser.add_argument('mobilenumber', type=str, required=True, location='json')
        args = parser.parse_args()

        # Create an InfoItem instance from the parsed arguments.
        info_item = InfoItem(**args)

        # Instantiate a validator visitor to validate the info item.
        validator = InfoItemValidator()
        # Use the accept method to apply validation logic to the info item.
        errors = info_item.accept(validator)

        # Check if there were any validation errors.
        if errors:
            # Return errors as JSON response with HTTP status code 400 (Bad Request).
            return jsonify({"status": "error", "errors": errors}), 400

        # Insert the info item into the database if validation passes.
        response = insert_info_item(**args)
        # Return a success response with the inserted info item details.
        return jsonify(response)

    # Handle PUT requests to update an existing info item by its ID.
    def put(self, item_id):
        parser = reqparse.RequestParser()
        print("item_id",item_id)
        parser.add_argument('id', type=str, location='json')
        parser.add_argument('firstname', type=str, required=True, location='json')
        parser.add_argument('lastname', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('uid', type=str, required=True, location='json')
        parser.add_argument('mobilenumber',type=str, required=True,location='json')

        args = parser.parse_args()
        response = update_info_item(
            item_id=item_id, 
            firstname=args['firstname'],
            lastname=args['lastname'], 
            email=args['email'],
            uid=args['uid'],
            mobilenumber=args['moobilenumber']
        )
        return jsonify(response)
    # Handle DELETE requests to remove an info item by its ID.
    def delete(self, item_id):
        return jsonify(delete_info_item(item_id=item_id))