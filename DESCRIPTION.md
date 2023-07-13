# Ruppell: powerful Python text extractor toolkit

## What is it?

**Ruppell** is a Python package to help in documents' text extraction.

## Main Features
Here are just a few of the things that ruppell does well:

  - Create datasets from multiple files.
  - Extract documents' text (pdf, docx, jpeg, jpg, png).
  - Create Pandas dataframe from documents' folder.
  - Convert documents to .txt files

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

## Example

```
>>> import ruppell
>>> ruppell.image_to_string('image.png')
'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer id bibendum sapien.'
```

## Supported Languages

The language codes are **ISO 639-2/B** or **ISO 639-2/T**.

All languages codes [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

## Contributing
	
If you think that we can do the Ruppell more powerful please contribute with this project. And let's improve it to help other developers.

Create a pull request or let's talk about something in issues. Thanks a lot.

## Author
Jorge Melgarejo, melgarejo.colarte@gmail.com

## License
[MIT](LICENSE)
