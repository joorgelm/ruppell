from unittest import TestCase
from src import ruppell


class TestRuppell(TestCase):

    def setUp(self) -> None:
        super(TestRuppell, self).setUp()
        self.ruppell = ruppell

    def test_image_to_string(self):
        extracted = self.ruppell.image_to_string(file_path='./data/image.png')
        self.assertIsNotNone(extracted)
        self.assertTrue(230 <= len(extracted) <= 270)

    def test_pdf_to_string(self):
        extracted = self.ruppell.pdf_to_string(file_path='./data/artigo.pdf')
        self.assertIsNotNone(extracted)
        self.assertTrue(10000 <= len(extracted) <= 11000)
