from flask import session, request, render_template
from pymongo import MongoClient
from implementation.controller import Controller


class DatenbankController(Controller):
    def __init__(self, server='localhost', port=27017, dbname='sportsday'):
        self.dbServer = server
        self.dbPort = port
        self.client = MongoClient(self.dbServer, self.dbPort)
        self.currentDB = self.client[dbname]

    def get_information(self, collection):
        self.information = []
        for document in self.currentDB[collection].find():
            self.information.append(document)
        return self.information

    def get_station_information(self, collection='station'):
        return self.currentDB[collection].find_one({'stationname': session['username']})

    def get_student_information(self, filter_param):
        return self.currentDB['students'].find_one(filter_param)

    def update_points(self, data):
        self.currentDB['students'].update_one({'number': data['number']},
                                              {'$set': {'points': data['points']}})
