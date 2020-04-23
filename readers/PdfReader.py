from .AbstractReader import AbstractReader
from pdfminer import high_level


class PdfReader(AbstractReader):

    @classmethod
    def load_file(cls, file_path):
        cls.file = file_path

    @classmethod
    def to_string(cls):
        return high_level.extract_text(pdf_file=cls.file)

