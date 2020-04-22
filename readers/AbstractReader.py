from abc import ABC, abstractmethod


class AbstractReader(ABC):

    def __init__(self):
        self.__file = None

    @classmethod
    @abstractmethod
    def load_file(cls, file_path):
        pass

    @classmethod
    @abstractmethod
    def to_string(cls):
        pass

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value
