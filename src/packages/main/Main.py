from ...controller.database import DatabaseController
from .abstract import AbstractMain


class Main(AbstractMain):
    def __init__(self):
        self.collection = 'students'

    def loadData(self):
        db = DatabaseController()
        students = db.get_information(self.collection)
        classes = db.get_information('class')

