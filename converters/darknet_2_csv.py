from PIL import Image
import csv

def darknet_2_csv(image_path, label_path, new_label_path):
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
            filename = "." + image_path[20:]
            width = int(float(label_data[4][:-2]) * img_width)
            height = int(float(label_data[3]) * img_height)
            class_cone = 0
            xmax = int(float(label_data[1]) * img_width + width/2)
            xmin = int(float(label_data[1]) * img_width - width/2)
            ymax = int(float(label_data[2]) * img_height + height/2)
            ymin = int(float(label_data[2]) * img_height - height/2)
 
            writer.writerow({'filename': filename, 'width': width,
            'height': height, 'class': class_cone , 'xmax': xmax,
            'xmin': xmin, 'ymax': ymax, 'ymin':ymin})


if __name__ == "__main__":
    darknet_2_csv("../images_munich/amz_2019/400131.jpg",
     "../labels_munich/amz/amz_2019/400131.txt", "")