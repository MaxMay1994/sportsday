from .. import Controller
from ...packages.ajax import Ajax
from ..database import DatabaseController

class AjaxController(Controller):
    __db = None

    def __init__(self):
        self.__db = DatabaseController()

    def schoolclass(self):
        schoolclasses = self.__db.get_classes()
        class_points = {}
        top_3 = {}

        for schoolclass in schoolclasses:
            class_points[schoolclass['classname']] = 0

            students = self.__db.get_students_by_class(schoolclass['classname'])

            for student in students:
                if not student['ill']:
                    class_points[schoolclass['classname']] += student['points']




