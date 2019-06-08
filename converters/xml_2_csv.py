import csv
import xml.etree.ElementTree as ET
from utils.utils import translate_label_map

def xml_2_csv(image_path, label_path, new_label_path, ref_lm, lm_list, key_words):
    print("------------------------------")
    in_file = open(label_path, 'r')
    out_file = open(new_label_path, 'w')

    tree = ET.parse(in_file)
    root = tree.getroot()

    s_path =image_path.split("/")
    filename = "./" + s_path[-3] + "/" + s_path[-2] + "/" + s_path[-1]

    fieldnames = ['filename', 'width', 'height', 'class', 
    'xmax', 'xmin', 'ymax', 'ymin']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    writer.writeheader()

    for obj in root.iter('object'):
        class_cone = obj.find('name').text

        ## CONVERT LABEL
        ## TODO: load_label_maps from arg
        class_cone = translate_label_map(ref_lm, lm_list, class_cone, key_words)

        ## GET BB PTS
        if(obj.find('bndbox') != None):
            xmlbox = obj.find('bndbox')
            xmin = int(float(xmlbox.find('xmin').text))
            xmax = int(float(xmlbox.find('xmax').text))
            ymin = int(float(xmlbox.find('ymin').text))
            ymax = int(float(xmlbox.find('ymax').text))

        elif(obj.find('polygon') != None):
            xmlbox = obj.find('polygon')
            x_list = [ float(xmlbox.find(x).text) for x in ['x1','x2','x3','x4'] ]
            y_list = [ float(xmlbox.find(y).text) for y in ['y1','y2','y3','y4'] ]

            xmin = int(min(x_list))
            xmax = int(max(x_list))
            ymin = int(min(y_list))
            ymax = int(max(y_list))

        
        writer.writerow({'filename': filename, 'width': xmax-xmin,
            'height': ymax-ymin, 'class': class_cone , 'xmax': xmax,
            'xmin': xmin, 'ymax': ymax, 'ymin':ymin})