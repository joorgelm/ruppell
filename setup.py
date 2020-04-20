# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGE_NAME = 'ruppell'
PACKAGE_DIR = 'src'

setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    url='https://github.com/joorgelm/ruppell',
    download_url='https://github.com/joorgelm/ruppell/archive/0.0.1.tar.gz',
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: PACKAGE_DIR},
    license='MIT License',
    author='Jorge Melgarejo',
    author_email='melgarejo.colarte@gmail.com',
    keywords='ocr text extractor',
    description=u'text extractor based in tesseract ocr',
    install_requires=[
        'Pillow~=7.0.0',
        'pytesseract~=0.3.1',
        'setuptools~=46.1.3',
        'pdfminer.six~=20200402',
        'docx2txt~=0.8',
        'pandas~=1.0.3'
    ],
)
