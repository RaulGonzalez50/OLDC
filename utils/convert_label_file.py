from converters.darknet_2_csv import darknet_2_csv
from functools import partial

def convert_jpg():
    return "jpg"

def convert_txt(image_path, label_path, new_label_path):
    darknet_2_csv(image_path, label_path, new_label_path)

def convert_xml():
    return "xml"

def convert_label_file(image_path, label_path, new_label_path):
    extension = label_path[-3:]

    switcher = {
            "jpg": convert_jpg,
            "xml": convert_xml,
            "txt": partial(convert_txt, image_path, label_path,
            new_label_path)
    }

    # Get the function from switcher dictionary
    func = switcher.get(extension, lambda: "Invalid format")
    # Execute the function
    res = func()
    print(res)

if __name__ == "__main__":
    convert_label_file("./images_munich/amz_2019/400131.jpg",
    "./labels_munich/amz/amz_2019/400131.txt",
    "prova.csv")
