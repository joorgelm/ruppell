from abc import ABC, abstractmethod


class AbstractReader(ABC):

    @classmethod
    @abstractmethod
    def load_file(cls, file_path):
        pass

    @classmethod
    @abstractmethod
    def to_string(cls):
        pass
