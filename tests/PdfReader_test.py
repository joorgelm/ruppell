from unittest import TestCase
from src.readers.PdfReader import PdfReader


class TestPdfReader(TestCase):

    def setUp(self) -> None:
        super(TestPdfReader, self).setUp()
        self.pdfReader = PdfReader()

    def test_load_file(self):
        self.pdfReader.load_file(file_path='./data/artigo.pdf')
        self.assertIsNotNone(self.pdfReader.file)
