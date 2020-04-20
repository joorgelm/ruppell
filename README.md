# Ruppell: powerful Python text extractor toolkit

## What is it?

**Ruppell** is a Python package to help in text extraction from documents.

## Main Features
Here are just a few of the things that ruppell does well:

  - Create datasets from multiple files.
  - Extract text from documents (pdf, docx, jpeg, jpg, png).
  - Create Pandas dataframe from folder of documents.
  - Create datasets from documents to .txt files.

## Where to get it

Binary installers for the latest released version are available at the [Python
package index](https://pypi.org/project/ruppell/).

```sh
pip install ruppell
```

## Dependencies
- [Pillow](https://github.com/python-pillow/Pillow)
- [Pytesseract](https://github.com/madmaze/pytesseract)
- [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- [Docx2txt](https://github.com/ankushshah89/python-docx2txt)
- [Pandas](https://github.com/pandas-dev/pandas)
- Python >= 3.6

## How to use

```python
from ruppell import ruppell


# Extract text from pdf
text = ruppell.pdf_to_string(file_path='file_path.pdf')


# Extract text from docx
text = ruppell.docx_to_string(file_path='file_path.docx')


# Extract text from image
text = ruppell.image_to_string(file_path='file_path.jpeg')


# Create pandas dataframe from documents folder
dataframe = ruppell.folder_to_dataframe(folder_path='folder_path')


# Create dict from documents folder
dict_out = ruppell.folder_to_dict(folder_path='folder_path')


# Create .txt files from documents folder
# A folder ./out will created in the same path of folder_path
ruppell.folder_to_txt(folder_path='folder_path')

```

## Contributing
	
If you think that we can do the Ruppell more powerful please contribute with this project. And let's improve it to help other developers.

Create a pull request or let's talk about something in issues. Thanks a lot.

## Author
Jorge Melgarejo, melgarejo.colarte@gmail.com

## License
[MIT](LICENSE)
