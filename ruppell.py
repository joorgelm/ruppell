from readers.ImageReader import ImageReader
from readers.PdfReader import PdfReader
from readers.DocxReader import DocxReader
from utils import utils
import pandas as pd
import calendar
import time
import os


def setup_language(language: str) -> None:
    ImageReader.set_language(language)


def image_to_string(file_path: str) -> str:
    ImageReader.load_file(file_path)
    return ImageReader.to_string()


def pdf_to_string(file_path: str) -> str:
    PdfReader.load_file(file_path)
    return PdfReader.to_string()


def docx_to_string(file_path: str) -> str:
    DocxReader.load_file(file_path)
    return DocxReader.to_string()


def folder_to_dict(folder_path: str) -> dict:

    out_dict = {'file_name': [], 'text_raw': []}

    for file in os.listdir(folder_path):

        file_extension = utils.get_extension_file(file)

        file_path = f'{folder_path}/{file}'

        text_raw = None

        if file_extension == 'pdf':
            text_raw = pdf_to_string(file_path)

        elif file_extension in ImageReader.IMAGE_TYPES:
            text_raw = image_to_string(file_path)

        elif file_extension == 'docx':
            text_raw = docx_to_string(file_path)

        if text_raw:
            out_dict['file_name'].append(file)
            out_dict['text_raw'].append(text_raw)

    return out_dict


def folder_to_txt(folder_path: str) -> str:

    dict_raw = folder_to_dict(folder_path)

    now = calendar.timegm(time.gmtime())

    out_path = f'{folder_path}/out_{now}/'

    utils.create_folder(out_path)

    for file, text_raw in zip(dict_raw['file_name'], dict_raw['text_raw']):

        utils.to_txt(text_raw=text_raw, file_name=file, out_path=out_path)

    print(f'The results are in {out_path}')

    return out_path


def folder_to_dataframe(folder_path: str) -> pd.DataFrame:
    return pd.DataFrame(data=folder_to_dict(folder_path))
