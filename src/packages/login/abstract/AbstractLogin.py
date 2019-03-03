import abc
from src.packages.AbstractObject import AbstractObject


class AbstractLogin(AbstractObject):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """this method sets the needed class member"""
        pass

    @abc.abstractmethod
    def get_login_information(self):
        """This method returns needed information from the database"""
        pass

    @abc.abstractmethod
    def validate_login_request(self):
        """this method validates the entered login data"""
        pass

    @abc.abstractmethod
    def login(self, information):
        """this method sets the session information if the return value of @validate_login_request was true"""
        pass

    @abc.abstractmethod
    def logout(self):
        """this method deletes all information in the session"""
        pass

    @abc.abstractmethod
    def hash_password(self, password, timestamp, salt):
        """this method creates the hash value of the given password"""
        pass
