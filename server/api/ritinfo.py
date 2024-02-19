import psycopg2
import yaml
import os
import pandas as pd
import numpy as np
import sys
import os
from .swen_610_db_utils import *

# Rebuilds the database tables using the specified SQL script.
# This could be seen as preparing the 'elements' (tables) for visitors (operations) in the Visitor pattern.
def rebuild_tables():
    exec_sql_file('infoDetail.sql')

# Retrieves all items from the InfoDetail table.
# In a Visitor pattern context, this could be considered as gathering all 'elements' for a potential 'visit'.
def list_info_items():
    """Fetches all records from the InfoDetail table."""
    result = exec_get_all('''SELECT * FROM InfoDetail''')
    return result

# Inserts a new item into the InfoDetail table and returns its ID.
# This can be linked to adding a new 'element' that could later be 'visited' by different operations or 'visitors'.
def insert_info_item(**kwargs):
    """
    Inserts a new information item into the database.
    
    Args:
        **kwargs: Details of the item to be inserted (firstname, lastname, email, uid, mobilenumber).
    
    Returns:
        The ID of the newly inserted item, allowing for identification in future 'visits'.
    """
    sql = '''INSERT INTO infoDetail (firstname, lastname, email, uid, mobileNum) VALUES (%s, %s, %s, %s, %s) RETURNING id;'''
    args = (kwargs.get('firstname'), kwargs.get('lastname'), kwargs.get('email'), kwargs.get('uid'), kwargs.get('mobilenumber'))
    inserted_id = exec_commit(sql, args)
    return inserted_id

# Updates an existing item in the InfoDetail table.
# Conceptually, this could be seen as modifying an 'element' before it receives further 'visits' by operations.
def update_info_item(**kwargs):
    """
    Updates details of an existing information item in the database.
    
    Args:
        **kwargs: New details for the item along with its ID.
    
    Returns:
        The ID of the updated item, ensuring it can still be identified for any 'visits'.
    """
    sql = '''UPDATE InfoDetail SET firstname=%s, lastname=%s, email=%s, uid=%s, mobileNum=%s WHERE id=%s RETURNING id;'''
    args = (kwargs['firstname'], kwargs['lastname'], kwargs['email'], kwargs['uid'], kwargs['mobilenumber'], kwargs['item_id'])
    updated_item = exec_commit(sql, args)
    return updated_item

# Deletes an item from the InfoDetail table.
# This could be viewed as removing an 'element' from the pool of items that can be 'visited'.
def delete_info_item(item_id):
    """
    Deletes an information item from the database.
    
    Args:
        item_id: The ID of the item to be deleted.
    
    Returns:
        The result of the delete operation, typically confirmation of deletion.
    """
    result = exec_commit('''DELETE FROM InfoDetail WHERE id = %s;''', (item_id,))
    return result
