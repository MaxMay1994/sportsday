from ...controller.database import DatabaseController

from .abstract.AbstractStudent import AbstractStudent


class Student(AbstractStudent):
    def __init__(self):
        pass

    def add_student(self, number, school_class):
        db = DatabaseController()
        return db.insert_student(number, school_class)

