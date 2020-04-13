# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='codigo-avulso-test-tutorial',
    version='0.0.1',
    url='https://github.com/joorgelm/ruppell',
    license='MIT License',
    author='Jorge Melgarejo',
    author_email='melgarejo.colarte@gmail.com',
    keywords='ocr text extractor',
    description=u'text extractor based in tesseract ocr',
    packages=find_packages(),
    install_requires=[],
)