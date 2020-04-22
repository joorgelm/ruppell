from .AbstractReader import AbstractReader
from PIL import Image
from pytesseract import pytesseract


class ImageReader(AbstractReader):

    IMAGE_TYPES = ['jpg', 'jpeg', 'png']

    __lang = 'eng'

    @staticmethod
    def set_language(lang):
        ImageReader.__lang = lang

    @classmethod
    def load_file(cls, file_path):
        cls.file = Image.open(file_path)

    @classmethod
    def to_string(cls):
        return pytesseract.image_to_string(cls.file, lang=ImageReader.__lang)
