from flask import session
from pymongo import MongoClient
from .. import Controller


class DatabaseController(Controller):
    def __init__(self, server='localhost', port=27017, dbname='sportsday'):
        self.dbServer = server
        self.dbPort = port
        self.client = MongoClient(self.dbServer, self.dbPort)
        self.currentDB = self.client[dbname]

    def get_information(self, collection):
        return self.currentDB[collection].find()

    def get_current_station(self, collection='station'):
        return self.currentDB[collection].find_one({'stationname': session['username']})

    def get_student_information(self, filter_param):
        return self.currentDB['students'].find_one(filter_param)

    def get_station_information(self, filter_param):
        return self.currentDB['students'].find_one(filter_param)

    def get_class_information(self, filter_param):
        return self.currentDB['class'].find_one(filter_param)

    def update_points(self, data):
        self.currentDB['students'].update_one({'number': data['number']},
                                              {'$set': {'points': data['points']}})

    def update_student_ill(self, student):
        self.currentDB['students'].update_one({'number': student['number']},
                                              {'$set': {'ill': student['ill']}})

    def get_stations(self):
        return self.currentDB['station'].find()

    def get_students(self):
        return self.currentDB['']

    def insert_station(self, form, auth):
        result = self.currentDB['station'].insert_one(
            {'stationname': form['stationname'], 'points': form['points'], 'area': form['area'], 'pin': auth['pin'],
             'description': form['description'], 'salt': auth['salt'], 'timestap': auth['timestamp']})

        if result is not False and result is not None:
            return True

        return False

    def get_classes(self):
        return self.currentDB['class'].find()

    def insert_class(self, form, number):
        result = self.currentDB['class'].insert_one(
            {'classname': form['classname'], 'number': number, 'amountStudents': form['amountStudents']})

    def insert_student(self, number, school_class):
        result = self.currentDB['students'].insert_one(
            {'number': number, 'class': school_class, 'points': 0, 'ill': False})

