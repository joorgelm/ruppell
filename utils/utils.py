import os


def get_extension_file(file_path: str) -> str:
    return file_path.split('.')[-1].lower()


def create_folder(folder_path: str):

    if not os.path.isdir(folder_path):
        try:
            os.mkdir(folder_path)
        except OSError:
            raise Exception('failed to create directory')


def to_txt(text_raw: str, file_name: str, out_path: str):

    with open(f'{out_path}/{file_name}.txt', "w") as output:
        output.write(text_raw)
        output.close()

