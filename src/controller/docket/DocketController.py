from src.controller import Controller
from src.controller.database import DatabaseController
from flask import Flask, render_template, make_response
import pdfkit
import pyqrcode
import math
import datetime
import os
import sys


class DocketController(Controller):
    db = DatabaseController()

    def __init__(self):
        pass

    @staticmethod
    def create_qr_code(self, key):
        url = 'http://www.klara-oppenheimer-schule.de/sportsday/statistics/'
        qr = pyqrcode.create(url+key)
        return qr.png('static/image/qrcode/' + key + '.png', scale=5)

    def generate_docket(self):
        db = DatabaseController()
        year = datetime.datetime.now().year
        path = os.path.dirname(sys.modules['__main__'].__file__)
        image_path = path+'/static/image/qrcode/'
        image_format = '.png'
        stations = db.get_information('station')
        row = 15
        column = 2
        station_table = [[0] * column for i in range(row)]

        for i in range(row):
            for j in range(column):
                if stations.count() > j + i*column:
                    station_table[i][j] = stations.__getitem__(j + i*column)

        # order by class
        students = db.get_information('students')

        row = math.ceil(students.count() / 3.0)
        column = 3
        students_table = [[0] * column for i in range(row)]

        for i in range(row):
            for j in range(column):
                if students.count() > j + i*column:
                    students_table[i][j] = students.__getitem__(j + i*column)

        for i in range(students.count()):
           self.create_qr_code(self, students.__getitem__(i)['number'])

        template = render_template('docket/docket.html',
                                   station_table=station_table,
                                   year=year,
                                   students_table=students_table,
                                   path=path,
                                   image_path=image_path,
                                   image_format=image_format
                                   )
        pdf = pdfkit.from_string(template, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=sportsday.pdf'
        return response


