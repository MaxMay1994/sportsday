import time
from random import randint
from flask import request
from src.controller.database import DatabaseController
from src.packages.login import Login
from src.packages.schoolclass.abstract.AbstractSchoolClass import AbstractSchoolClass


class SchoolClass(AbstractSchoolClass):
    pass

    def add_class(self):
        db = DatabaseController()

        # DO-WHILE ???
        while True:
            number = randint(100, 999)
            if db.get_class_information({'number': number}) is None:
                break

        #login = Login()
        #auth = {'timestamp': time.time(), 'salt': randint(10, 99), 'pin': ''}

        #auth['pin'] = login.hash_password(request.form['pin'], auth['timestamp'], auth['salt'])
        return db.insert_class(request.form, number)
