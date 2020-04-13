from readers.ImageReader import ImageReader


def image_to_string(file_path):
    ImageReader.load_file(file_path)
    return ImageReader.to_string()
