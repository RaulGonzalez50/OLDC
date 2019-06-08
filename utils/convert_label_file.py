from converters.darknet_2_csv import darknet_2_csv
from converters.xml_2_csv import xml_2_csv
from functools import partial

## SWITCH FUNCITONS
def convert_txt(image_path, label_path, new_label_path, ref_lm, lm_list, key_words):
    darknet_2_csv(image_path, label_path, new_label_path, ref_lm, lm_list, key_words)

def convert_xml(image_path, label_path, new_label_path, ref_lm, lm_list, key_words):
    xml_2_csv(image_path, label_path, new_label_path, ref_lm, lm_list, key_words)

## COINVERTER
def convert_label_file(image_path, label_path, new_label_path, ref_lm, lm_list, key_words):
    extension = label_path[-3:]

    switcher = {
            "xml": partial(convert_xml, image_path, label_path,
            new_label_path, ref_lm, lm_list, key_words),
            "txt": partial(convert_txt, image_path, label_path,
            new_label_path, ref_lm, lm_list, key_words)
    }

    # Get the function from switcher dictionary
    func = switcher.get(extension, lambda: "Invalid format")
    # Execute the function
    func()
