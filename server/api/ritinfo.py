import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from .swen_610_db_utils import *

def rebuild_tables():
    exec_sql_file('infoDetail.sql')

def list_info_items():
    """ Return all items as a list of tuples. """
    result = exec_get_all('''SELECT * FROM InfoDetail''')
    return result

def insert_info_item(**kwargs):
    """Insert item into the database and return its ID."""
    print("Received DATA:", kwargs)
    firstname = kwargs.get('firstname')
    lastname = kwargs.get('lastname')
    email = kwargs.get('email')
    uid = kwargs.get('uid')
    mobilenumber = kwargs.get('mobilenumber')
    sql = '''INSERT INTO infoDetail (firstname, lastname, email, uid, mobileNum) 
             VALUES (%s, %s, %s, %s, %s) RETURNING id;'''
    args = (firstname, lastname, email, uid, mobilenumber)
    inserted_id = exec_commit(sql, args)
    print(inserted_id)
    return inserted_id


def update_info_item(**kwargs):
    """ Update a food item in the database and return its details. """
    item_id = kwargs.get('item_id')
    print("id", item_id)
    firstname = kwargs.get('firstname')
    lastname = kwargs.get('lastname')
    email = kwargs.get('email')
    uid = kwargs.get('uid')
    mobilenumber = kwargs.get('mobilenumber')

    sql = '''UPDATE InfoDetail SET firstname = %s, lastname = %s ,email = %s, uid = %s, mobileNum=%s
             WHERE id = %s RETURNING id;'''
    updated_item = exec_commit(sql, (firstname, lastname ,email, uid, item_id,mobilenumber))

    print(updated_item)
    return updated_item


def delete_info_item(item_id):
    """ Delete a food item from the database. """
    result = exec_commit('''DELETE FROM InfoDetail WHERE id = %s;''', (item_id,))
    return result
