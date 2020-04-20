from unittest import TestCase
from src.readers.ImageReader import ImageReader


class TestImageReader(TestCase):

    def setUp(self) -> None:
        super(TestImageReader, self).setUp()
        self.imageReader = ImageReader()

    def test_load_file(self):
        self.imageReader.set_language('por')
        self.imageReader.load_file(file_path='./data/image.png')
        self.assertIsNotNone(self.imageReader.file)

    def test_set_language(self):
        self.imageReader.set_language('por+eng')
        self.assertTrue(self.imageReader._ImageReader__lang == 'por+eng')
