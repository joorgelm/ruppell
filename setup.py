# -*- coding: utf-8 -*-
from setuptools import setup

with open("DESCRIPTION.md", "r") as fh:
    long_description = fh.read()

PACKAGE_NAME = 'ruppell'
PACKAGES = ['', 'readers', 'utils']
VERSION = '1.0.0'
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
    long_description_content_type='text/markdown',
    description=DESCRIPTION,
    long_description=long_description,
    install_requires=[
        'Pillow~=10.0.0',
        'pytesseract~=0.3.10',
        'setuptools~=68.0.0',
        'pdfminer.six==20221105',
        'docx2txt~=0.8',
        'pandas~=2.0.3'
    ],
)
