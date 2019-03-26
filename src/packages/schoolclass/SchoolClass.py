import random
from flask import request
from ...controller.database import DatabaseController
from ..schoolclass.abstract.AbstractSchoolClass import AbstractSchoolClass


class SchoolClass(AbstractSchoolClass):
    pass

    def add_class(self):
        db = DatabaseController()

        if request.form['amountStudents'].isdigit():
            # DO-WHILE ???
            while True:
                number = random.randint(100, 999)
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

                    student_list = db.get_students_by_class(class_name)
                    amount_students = int(request.form['amountStudents-' + class_name])
                    students = student_list.count()

                    if students > amount_students:
                        self.remove_students(students - amount_students, student_list)
                    elif students < amount_students:
                        self.add_students(amount_students - students, class_name)

                    if request.form['classname-'+class_name] != class_name:
                        student_list = db.get_students_by_class(class_name)

                        for student in student_list:
                            db.update_student({'number': student['number']}, {'$set': {'class': request.form['classname-'+class_name]}})

                    if result is not None:
                        return True

            elif button[0:6] == "delete":
                result = db.delete_class(class_name)

                if result is not None:
                    db.delete_students({'class': class_name})
                    return True

        return None

    def validate_request_data(self, class_name):
        if not request.form['amountStudents-' + class_name].isdigit():
            return False

        return True

    def add_students(self, students, school_class):
        db = DatabaseController()
        number_list = []

        for student in range(students):
            while True:
                student_number = random.randint(10, 99)
                if student_number not in number_list:
                    number_list.append(student_number)
                    break
            class_number = db.get_class_information({'classname': school_class}).get('number')
            db.insert_student(str(class_number) + str(student_number), school_class)

    def remove_students(self, students, student_cursor):
        student_list = student_cursor.clone()
        db = DatabaseController()

        for i in range(students):
            for student in student_list:
                db.delete_student(student['number'])
                student_list.next()
                break
