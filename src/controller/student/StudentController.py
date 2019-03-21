from src.controller.database import DatabaseController
from src.controller import Controller
from src.packages.student import Student
import random
from flask import request


class StudentController(Controller):
    def __init__(self):
        pass

    def add_students(self, school_class, amount):
        student = Student()
        db = DatabaseController()
        number_list = []

        for i in range(int(amount)):
            while True:
                student_number = random.randint(10, 99)
                if student_number not in number_list:
                    number_list.append(student_number)
                    break
            class_number = db.get_class_information({'classname': request.form['classname']}).get('number')
            student.add_student(str(class_number) + str(student_number), school_class)


