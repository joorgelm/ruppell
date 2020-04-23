from unittest import TestCase
import ruppell
import pandas as pd
import os


class TestRuppell(TestCase):

    TEST_DATA = './data/'

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

    def test_docx_to_string(self):
        extracted = self.ruppell.docx_to_string(file_path='./data/teste.docx')
        self.assertIsNotNone(extracted)
        self.assertTrue(extracted == 'teste')

    def test_folder_to_dict(self):
        extracted = self.ruppell.folder_to_dict(folder_path=TestRuppell.TEST_DATA)
        self.assertTrue(type(extracted) == dict)

    def test_folter_to_txt(self):
        folder_path = TestRuppell.TEST_DATA
        out_path = f'{folder_path}/out/'

        self.ruppell.folder_to_txt(folder_path=folder_path)

        self.assertTrue(os.path.isdir(out_path))

        number_of_files = len(os.listdir(out_path))
        self.assertTrue(number_of_files > 0)

    def test_folder_to_dataframe(self):
        extracted = self.ruppell.folder_to_dataframe(folder_path=TestRuppell.TEST_DATA)
        self.assertTrue(type(extracted) == pd.DataFrame)

