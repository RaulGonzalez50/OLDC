import csv
import os

def merge_csv(images_dir, labels_dir, image_set):
        ## INFO MSG
        print("MERGING " + image_set + " CSV ...")

        with open(images_dir + image_set + ".csv", mode='w') as merged_csv:
                fieldnames = ['filename', 'width', 'height', 'class', 
                'xmax', 'xmin', 'ymax', 'ymin']
                writer = csv.DictWriter(merged_csv, fieldnames=fieldnames)
                writer.writeheader()

                csv_files = os.listdir(labels_dir + image_set + "/")
                csv_files.sort()

                for csv_file in csv_files:
                        f = open(labels_dir + image_set + "/" + csv_file, "r")
                        is_header = True

                        for line in f:
                                if(is_header):
                                        is_header = False
                                else:
                                        label_data = line.split(',')       
                                        writer.writerow({'filename': label_data[0], 'width': label_data[1],
                                        'height': label_data[2], 'class': label_data[3] , 'xmax': label_data[4],
                                        'xmin': label_data[5], 'ymax': label_data[6], 'ymin':label_data[7]})

def translate_label_map(your_label_map, data_label_map, label):
        ## TODO: Complete function
        index = 0
        return index