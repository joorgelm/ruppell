from unittest import TestCase
from src.readers.DocxReader import DocxReader


class TestDocxReader(TestCase):

    def setUp(self) -> None:
        super(TestDocxReader, self).setUp()
        self.DocxReader = DocxReader()

    def test_load_file(self):
        self.DocxReader.load_file('./data/teste.docx')
        self.assertIsNotNone(self.DocxReader.file)
