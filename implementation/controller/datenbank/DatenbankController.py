from flask import session, request, render_template
import json
from pymongo import MongoClient
from implementation.controller import Controller


class DatenbankController(Controller):
    def __init__(self, server='localhost', port=27017, dbname='sportsday'):
        self.dbServer = server
        self.dbPort = port
        self.client = MongoClient(self.dbServer, self.dbPort)
        self.currentDB = self.client[dbname]

    def get_login_information(self, collection):
        self.login_information = []
        for document in self.currentDB[collection].find():
            self.login_information.append(document)
        return self.login_information
