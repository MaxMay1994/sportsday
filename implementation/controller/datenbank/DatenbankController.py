from flask import session, request, render_template
from pymongo import MongoClient
from implementation.controller import Controller


class DatenbankController(Controller):
    def __init__(self, server='localhost', port=27017, dbname='Test'):
        self.dbServer = server
        self.dbPort = port
        self.client = MongoClient(self.dbServer, self.dbPort)
        self.currentDB = self.client[dbname]

    def get_login_information(self):
        for document in self.currentDB['collection1'].find():
            print(document)
        return self.currentDB['collection1'].find()[0]

