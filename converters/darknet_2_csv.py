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

            if '\n' in label_data[0]:
                continue

            if 'nan' in label_data:
                continue

            s_path =image_path.split("/")
            filename = "./" + s_path[-3] + "/" + s_path[-2] + "/" + s_path[-1]
            
            if float(label_data[1]) < 1.0000000:
                width = int(float(label_data[3]) * img_width)
                height = int(float(label_data[4][:-2]) * img_height)

                ## CONVERT LABEL
                class_cone = translate_label_map(ref_lm, lm_list, label_data[0], key_words)

                if class_cone is None:
                    continue

                xmax = int(float(label_data[1]) * img_width + width/2)
                xmin = int(float(label_data[1]) * img_width - width/2)
                ymax = int(float(label_data[2]) * img_height + height/2)
                ymin = int(float(label_data[2]) * img_height - height/2)
            else:
                ## CONVERT LABEL
                class_cone = translate_label_map(ref_lm, lm_list, label_data[0], key_words)

                if class_cone is None:
                    continue

                xmax = int(label_data[1]) 
                xmin = int(label_data[3])
                ymax = int(label_data[2])
                ymin = int(label_data[4])

                width = xmax-xmin
                height = ymax-ymin

 
            writer.writerow({'filename': filename, 'width': width,
            'height': height, 'class': class_cone , 'xmax': xmax,
            'xmin': xmin, 'ymax': ymax, 'ymin':ymin})
