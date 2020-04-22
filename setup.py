# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGE_NAME = 'ruppell'
PACKAGES = ['', 'readers', 'utils']
VERSION = '0.0.4'
DESCRIPTION = "Ruppell is a Python package to help in text extraction from documents."

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    url='https://github.com/joorgelm/ruppell',
    download_url=f'https://github.com/joorgelm/ruppell/archive/{VERSION}.tar.gz',
    package_dir={PACKAGE_NAME: ''},
    packages=PACKAGES,
    license='MIT License',
    author='Jorge Melgarejo',
    author_email='melgarejo.colarte@gmail.com',
    keywords='ocr text extractor',
    description=u'text extractor based in tesseract ocr',
    install_requires=[
        'Pillow>=7.0.0',
        'pytesseract>=0.3.1',
        'setuptools>=46.1.3',
        'pdfminer.six>=20200402',
        'docx2txt>=0.8',
        'pandas>=1.0.3'
    ],
)
