from src.readers.ImageReader import ImageReader
from src.readers.PdfReader import PdfReader


def image_to_string(file_path):
    ImageReader.load_file(file_path)
    return ImageReader.to_string()


def pdf_to_string(file_path):
    PdfReader.load_file(file_path)
    return PdfReader.to_string()


if __name__ == '__main__':
    teste = pdf_to_string('../tests/data/artigo.pdf')
    print(teste)
