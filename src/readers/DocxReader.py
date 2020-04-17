from .AbstractReader import AbstractReader
from docx2txt import docx2txt


class DocxReader(AbstractReader):

    @classmethod
    def load_file(cls, file_path):
        cls.file = file_path

    @classmethod
    def to_string(cls):
        return docx2txt.process(cls.file)
