import json
from .. import Controller
from ...packages.ajax import Ajax
from ..database import DatabaseController


class AjaxController(Controller):
    __db = None

    def __init__(self):
        self.__db = DatabaseController()

    def top_3_class(self):
        schoolclasses = self.__db.get_classes()
        class_points = {}
        top_3 = {}
        top_points = []
        top_classes = {}

        for schoolclass in schoolclasses:
            class_points[schoolclass['classname']] = 0

            students = self.__db.get_students_by_class(schoolclass['classname'])

            for student in students:
                if not student['ill']:
                    class_points[schoolclass['classname']] += student['points']

            class_points[schoolclass['classname']] = float(class_points[schoolclass['classname']]) / students.count()

        point_list = list(class_points.values())

        for j in range(0, 3):
            value = max(point_list)
            top_points.append(value)
            point_list.remove(value)

        a = 0

        for point in top_points:
            for i in class_points:
                if point == class_points[i] and i not in top_classes:
                    if a < 3:
                        top_classes[i] = True
                        top_3[a] = {'classname': i, 'points': point}
                        a += 1
                        break

        top_3_json = json.dumps(top_3)

        return top_3_json

    def top_3_student(self):
        top_students = []
        top_3 = {}
        top_points = []
        checked_students = {}
        a = 0

        students = list(self.__db.get_students())

        for student in students:
            top_students.append(student['points'])

        for j in range(0, 3):
            value = max(top_students)
            top_points.append(value)
            top_students.remove(value)

        #students.rewind()

        for point in top_points:
            for student in students:
                if point == student['points'] and student['number'] not in checked_students:
                    if a < 3:
                        checked_students[student['number']] = True
                        top_3[a] = {'studentnumber': student['number'], 'points': point}
                        a += 1
                        break

        top_3_json = json.dumps(top_3)

        return top_3_json

    def student_class(self, student_id):
        current_student = self.__db.get_student_information({'number': str(student_id)})
        schoolclass = self.__db.get_class_information({'classname': current_student['class']})
        top_3 = {0: {'studentnumber': current_student['number'], 'points': current_student['points']}}
        top_points = []
        point_list = []
        top_students = {}

        students = list(self.__db.get_students_by_class(schoolclass['classname']))

        for student in students:
            point_list.append(student['points'])

        for j in range(1, 4):
            value = max(point_list)
            top_points.append(value)
            point_list.remove(value)

        a = 1

        #students.rewind()
        for point in top_points:
            for student in students:
                if point == student['points'] and student['number'] not in top_students:
                    if a < 4:
                        top_students[student['number']] = True
                        top_3[a] = {'studentnumber': student['number'], 'points': point}
                        a += 1
                        break

        top_3_json = json.dumps(top_3)

        return top_3_json

    def student_global(self, student_id):
        current_student = self.__db.get_student_information({'number': str(student_id)})

        top_students = []
        top_3 = {0: {'studentnumber': current_student['number'], 'points': current_student['points']}}
        top_points = []
        checked_students = {}
        a = 1

        students = list(self.__db.get_students())

        for student in students:
            top_students.append(student['points'])

        for j in range(1, 4):
            value = max(top_students)
            top_points.append(value)
            top_students.remove(value)

        #students.rewind()
        for point in top_points:
            for student in students:
                if point == student['points'] and student['number'] not in checked_students:
                    if a < 4:
                        checked_students[student['number']] = True
                        top_3[a] = {'studentnumber': student['number'], 'points': point}
                        a += 1
                        break

        top_3_json = json.dumps(top_3)

        return top_3_json
