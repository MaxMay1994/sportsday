import abc

from src.packages.AbstractObject import AbstractObject


class AbstractStation(AbstractObject):

    def __init__(self):
        pass

    @abc.abstractmethod
    def update_points(self):
        """updates the points of the given student"""
        pass

    @abc.abstractmethod
    def manage_station(self):
        """Logic to manage Stations"""
        pass

    @abc.abstractmethod
    def add_station(self):
        """Create new Station"""
        pass
