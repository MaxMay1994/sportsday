from random import randint
from flask import request
from src.controller.database import DatabaseController
from src.packages.schoolclass.abstract.AbstractSchoolClass import AbstractSchoolClass


class SchoolClass(AbstractSchoolClass):
    pass

    def add_class(self):
        db = DatabaseController()

        if request.form['amountStudents'].isdigit():
            # DO-WHILE ???
            while True:
                number = randint(100, 999)
                if db.get_class_information({'number': number}) is None:
                    break

            return db.insert_class(request.form, number)
        return False

    def manage_class(self):
        db = DatabaseController()

        if request.method == 'POST':
            button = request.form.copy().popitem()[0]
            delimiter_position = button.find('-')

            # it's kinda weird, because we need the name of the station without -
            # that's why we add to the position of the delimiter +1
            class_name = button[delimiter_position + 1:]

            if button[0:4] == "save":
                success = self.validate_request_data(class_name)
                if success:
                    search_dict = {'classname': class_name}
                    update_dict = {"$set": {"classname": request.form['classname-' + class_name],
                                            "amountStudents": int(request.form['amountStudents-' + class_name])}}

                    result = db.update_class(search_dict, update_dict)

                    if result is not None:
                        return True

            elif button[0:6] == "delete":
                result = db.delete_class(class_name)

                if result is not None:
                    return True

        return False

    def validate_request_data(self, class_name):
        if not request.form['amountStudents-' + class_name].isdigit():
            return False

        return True
