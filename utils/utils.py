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

def load_label_map(label_map_path):
        label_map_list = []
        if "txt" in label_map_path.split(".")[-1]:
                f = open(label_map_path, "r")
                for line in f:
                        label_map_list.append(line[:-1])
                return label_map_list
        else:
                ## TODO: Implement .pbtxt coversion
                return label_map_list


def translate_label_map(ref_lm, data_label_map, label, key_words):
        if key_words:
                try:
                        lm_val = int(label)
                        lm_name = data_label_map[lm_val]
                except ValueError:
                        lm_name = label 
    
                for c in key_words:
                        for word in c:
                                if word in lm_name:
                                        index = key_words.index(c)
                                        if index == 2:
                                                if ("big" in lm_name or "Big" in lm_name or "BIG" in lm_name):
                                                        index += 1
                                        return index
        else:
                try:
                        lm_val = int(label)
                except ValueError:
                        lm_val = ref_lm.index(label)
                return lm_val