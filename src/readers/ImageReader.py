from .AbstractReader import AbstractReader
from PIL import Image
from pytesseract import pytesseract


class ImageReader(AbstractReader):

    __file = None

    @classmethod
    def load_file(cls, file_path):
        cls.__file = Image.open(file_path)

    @classmethod
    def to_string(cls):
        return pytesseract.image_to_string(cls.__file, lang='por')

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value
