from PIL import Image
import os

formats = ("JPG", "PNG", "WebP", "JPEG")



def file_conversion(source, des_path, new_format):
    image = Image.open(source)
    file_name = get_file_name(source)
    image.save(f"{des_path}" + "\\" f"{file_name}{new_format}")

    image.save(f"{des_path}{new_format}")
    return


def path_conversion(source, des_path, new_format):
    source_file = os.listdir(source)
    print(source_file)
    print(source)

    for file_name in source_file:
        image = Image.open(f"{source}" + "\\" f"{file_name}")
        extract_file_name = get_file_name(file_name)
        image.save(f"{des_path}" + "\\" f"{extract_file_name}{new_format}")


def get_file_name(source):
    if source.find("\\"):
        file_name = source.split("\\")[-1].split('.')[0]
    else:
        file_name = source.split('.')[0]
    return file_name




def detect_file(source, des_path, new_format):
    try:
        try:
            path_conversion(source, des_path, new_format)
        except NotADirectoryError:
            file_conversion(source, des_path, new_format)
    except (NameError, PermissionError):
        return False


def main_file(source, des_path, new_format):
    detect_file(source, des_path, new_format)

