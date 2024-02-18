from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from flask import jsonify
from .swen_610_db_utils import *
from .ritinfo import *
import json


# class Init(Resource):
#     def post(self):
#         rebuild_tables()

# class Version(Resource):
#     def get(self):
#         return (exec_get_one('SELECT VERSION()'))

class InfoDetails(Resource):
    def get(self):
        return jsonify(list_info_items())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, location='json')
        parser.add_argument('firstname', type=str, required=True, location='json')
        parser.add_argument('lastname', type=str, required=True, location='json')
        parser.add_argument('email', type=str, required=True, location='json')
        parser.add_argument('uid', type=str, required=True, location='json')
        parser.add_argument('mobilenumber', type=str, required=True, location='json')
        args = parser.parse_args()
        print("Received Data:", args)
        response = insert_info_item(
            firstname=args['firstname'],
            lastname=args['lastname'], 
            email=args['email'],
            uid=args['uid'],
            mobilenumber=args['mobilenumber']
        )
        return jsonify(response)


    
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

    def delete(self, item_id):
        return jsonify(delete_info_item(item_id=item_id))