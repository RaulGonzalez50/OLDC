import csv
import xml.etree.ElementTree as ET

def xml_2_csv(image_path, label_path, new_label_path):
    print("converting xml ...")
    print(image_path)
    print(label_path)
    in_file = open(label_path, 'r')
    out_file = open(new_label_path, 'w')

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')

    width = int(size.find('width').text)
    height = int(size.find('height').text)

    filename = "." + image_path[20:]

    fieldnames = ['filename', 'width', 'height', 'class', 
    'xmax', 'xmin', 'ymax', 'ymin']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    writer.writeheader()

    for obj in root.iter('object'):
        class_cone = obj.find('name').text

        ## TODO: insert label conversion
        class_cone = 0

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

        
        writer.writerow({'filename': filename, 'width': width,
            'height': height, 'class': class_cone , 'xmax': xmax,
            'xmin': xmin, 'ymax': ymax, 'ymin':ymin})