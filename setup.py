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
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: PACKAGE_DIR},
    license='MIT License',
    author='Jorge Melgarejo',
    author_email='melgarejo.colarte@gmail.com',
    keywords='ocr text extractor',
    description=u'text extractor based in tesseract ocr',
    install_requires=[],
)
