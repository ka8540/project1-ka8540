# Import necessary Flask extensions and utility functions.
from flask_restful import Resource, reqparse, request
from flask import jsonify
from .swen_610_db_utils import *  
from .ritinfo import * 
import json

# InfoItem class represents an entity and acts as an "Element" in the Visitor pattern.
# It contains data related to a user and can accept visitors to perform various operations.
class InfoItem:
    def __init__(self, firstname, lastname, email, uid, mobilenumber):
        # Initialization with user details.
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.uid = uid
        self.mobilenumber = mobilenumber

    # The accept method allows the Visitor to perform operations on the InfoItem instance.
    # This method is crucial for implementing the Visitor pattern, enabling operations without changing the class.
    def accept(self, visitor):
        return visitor.visit_info_item(self)

# InfoItemVisitor acts as the base class for any visitors that perform operations on InfoItems.
# This follows the Visitor pattern by declaring a visit operation for the InfoItem elements.
class InfoItemVisitor:
    def visit_info_item(self, info_item):
        # Intended to be overridden by concrete visitors with specific implementations.
        raise NotImplementedError

# Concrete visitor for validating InfoItem instances.
# Implements the InfoItemVisitor interface and provides specific validation logic.
class InfoItemValidator(InfoItemVisitor):
    def visit_info_item(self, info_item):
        # Validation logic to ensure the email address format is correct.
        errors = []
        if '@' not in info_item.email:
            errors.append('Invalid email address')
        return errors

# InfoDetails resource class for CRUD operations on info items via RESTful APIs.
# Demonstrates the use of the Visitor pattern in a web application context.
class InfoDetails(Resource):
    def get(self):
        # Fetch and return all info items, demonstrating retrieval without direct element manipulation.
        return jsonify(list_info_items())

    def post(self):
        # Parse and validate incoming data, showcasing how an element can accept a visitor for validation.
        parser = reqparse.RequestParser()
        # Parsing request data.
        parser.add_argument('firstname', type=str, required=True, location='json')
        parser.add_argument('lastname', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('uid', type=str, required=True, location='json')
        parser.add_argument('mobilenumber', type=str, required=True, location='json')
        args = parser.parse_args()

        # Creating an InfoItem element and accepting a validation visitor.
        info_item = InfoItem(**args)
        validator = InfoItemValidator()  # The visitor instance.
        errors = info_item.accept(validator)  # Element accepts visitor.

        if errors:
            # If validation fails, return errors.
            return jsonify({"status": "error", "errors": errors}), 400

        # If validation passes, insert the info item into the database.
        response = insert_info_item(**args)
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