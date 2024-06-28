#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from bson.objectid import ObjectId


# In[3]:


class AnimalShelter(object):
    """ CRUD operations for animal collection in MongoDB """
    #
    # Initialization
    #
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31425
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    #
    # Create new entry
    #
    def create(self, data) -> bool: # data should be dictionary
        if data is not None:
            self.database.animals.insert_one(data) 
            return True
        else:
            raise Exception("Nothing to save, because 'data' parameter is empty")
            return False

    #
    # Query an entry
    #
    def read(self, query) -> list: # query should be "{'key':'value'}"
        if query is not None:
            found = list(self.database.animals.find(query))
            return found
        else:
            raise Exception("Nothing to search, because 'query' parameter is empty")

    #
    # Update an entry
    #
    def update(self, toUpdate, updates) -> int: # toUpdate should be "{'key':'value'}"
        if toUpdate and updates is not None:    # and updates "{'$set':{'key1':'value1', 'key2':'value2', etc.}}"  
            modified = self.database.animals.update_many(toUpdate, updates)
            return modified.modified_count
        else:
            raise Exception("Cannot update, a parameter was left empty")

    #
    # Delete an entry
    #
    def delete(self, deleted) -> int: # deleted should be "{'key':'value'}"   
        if deleted is not None:
            modified = self.database.animals.delete_many(deleted)
            return modified.deleted_count 
        else:
            raise Exception("Nothing to delete, because 'deleted' parameter is empty")


# In[ ]:




