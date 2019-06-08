from PIL import Image
import csv
from utils.utils import translate_label_map

def darknet_2_csv(image_path, label_path, new_label_path, ref_lm, lm_list, key_words):
    ## GET IMG SHAPE
    im = Image.open(image_path)
    img_width, img_height = im.size

    ## FOR EACH LINE CONVERT ANNOTATION
    with open(new_label_path, mode='w') as csv_labels:
        fieldnames = ['filename', 'width', 'height', 'class', 
        'xmax', 'xmin', 'ymax', 'ymin']
        writer = csv.DictWriter(csv_labels, fieldnames=fieldnames)
        writer.writeheader()

        f = open(label_path, "r")
        for line in f:
            label_data = line.split(' ')

            s_path =image_path.split("/")
            filename = "./" + s_path[-3] + "/" + s_path[-2] + "/" + s_path[-1]

            width = int(float(label_data[4][:-2]) * img_width)
            height = int(float(label_data[3]) * img_height)
            
            print(label_data[0])
            ## CONVERT LABEL
            class_cone = translate_label_map(ref_lm, lm_list, label_data[0], key_words)

            if class_cone is None:
                continue

            xmax = int(float(label_data[1]) * img_width + width/2)
            xmin = int(float(label_data[1]) * img_width - width/2)
            ymax = int(float(label_data[2]) * img_height + height/2)
            ymin = int(float(label_data[2]) * img_height - height/2)
 
            writer.writerow({'filename': filename, 'width': width,
            'height': height, 'class': class_cone , 'xmax': xmax,
            'xmin': xmin, 'ymax': ymax, 'ymin':ymin})
