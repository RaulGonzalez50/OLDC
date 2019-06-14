import os, os.path, sys
from math import trunc
import random
from utils.convert_label_file import convert_label_file
from utils.utils import merge_csv, load_label_map
import glob

## SET DATASET'S FOLDER NAME
PATH_TO_DST_DATASET_FOLDER = "../"
DST_FOLDER_NAME = "MERGED_MUNICH_DATASET"

## SET PERCENTAGE OF DATA USED FOR TEST AND VALIDATION
VAL_PERCENTAGE = 0.1
TEST_PERCENTAGE = 0.1

## SET FOLDERS TO BE MERGED
# END directories with '/'
# SRC_IMG_DIRS = ["../../DATASET_TEAMS (copy)/amz/", "../../DATASET_TEAMS (copy)/bme/", "../../DATASET_TEAMS (copy)/dhbw/",
# "../../DATASET_TEAMS (copy)/DimitrisMartinArampatzis/", "../../DATASET_TEAMS (copy)/driverless_UPC/", "../../DATASET_TEAMS (copy)/elbflorace/",
# "../../DATASET_TEAMS (copy)/eufs/", "../../DATASET_TEAMS (copy)/fast-forest/", "../../DATASET_TEAMS (copy)/gfr/",
# "../../DATASET_TEAMS (copy)/high-octane/", "../../DATASET_TEAMS (copy)/itu/", "../../DATASET_TEAMS (copy)/kth/",
# "../../DATASET_TEAMS (copy)/tallinn/","../../DATASET_TEAMS (copy)/mms/", "../../DATASET_TEAMS (copy)/scut/", "../../DATASET_TEAMS (copy)/starkstrom/",
# "../../DATASET_TEAMS (copy)/unicamp/", "../../DATASET_TEAMS (copy)/vermilion/"] ## Source directory of the images

# SRC_LBLS_DIRS = ["../../DATASET_TEAMS (copy)/amz_labels/", "../../DATASET_TEAMS (copy)/bme_labels/", "../../DATASET_TEAMS (copy)/dhbw_labels/",
# "../../DATASET_TEAMS (copy)/DimitrisMartinArampatzis_labels/", "../../DATASET_TEAMS (copy)/driverless_UPC_labels/",
# "../../DATASET_TEAMS (copy)/elbflorace_labels/", "../../DATASET_TEAMS (copy)/eufs_labels/", "../../DATASET_TEAMS (copy)/fast-forest_labels/",
# "../../DATASET_TEAMS (copy)/gfr_labels/", "../../DATASET_TEAMS (copy)/high-octane_labels/", "../../DATASET_TEAMS (copy)/itu_labels/",
# "../../DATASET_TEAMS (copy)/kth_labels/", "../../DATASET_TEAMS (copy)/tallinn_labels/","../../DATASET_TEAMS (copy)/mms_labels/",
# "../../DATASET_TEAMS (copy)/scut_labels/", "../../DATASET_TEAMS (copy)/starkstrom_labels/", "../../DATASET_TEAMS (copy)/unicamp_labels/",
# "../../DATASET_TEAMS (copy)/vermilion_labels/"] ## Source directory of the labels


SRC_IMG_DIRS = ["../../DATASET_TEAMS (copy)/amz/", "../../DATASET_TEAMS (copy)/bme/",
"../../DATASET_TEAMS (copy)/DimitrisMartinArampatzis/", "../../DATASET_TEAMS (copy)/elbflorace/",
"../../DATASET_TEAMS (copy)/eufs/", "../../DATASET_TEAMS (copy)/fast-forest/",
"../../DATASET_TEAMS (copy)/high-octane/", "../../DATASET_TEAMS (copy)/itu/", "../../DATASET_TEAMS (copy)/kth/",
"../../DATASET_TEAMS (copy)/tallinn/","../../DATASET_TEAMS (copy)/mms/", "../../DATASET_TEAMS (copy)/scut/", "../../DATASET_TEAMS (copy)/starkstrom/",
"../../DATASET_TEAMS (copy)/unicamp/", "../../DATASET_TEAMS (copy)/vermilion/"] ## Source directory of the images

SRC_LBLS_DIRS = ["../../DATASET_TEAMS (copy)/amz_labels/", "../../DATASET_TEAMS (copy)/bme_labels/",
"../../DATASET_TEAMS (copy)/DimitrisMartinArampatzis_labels/",
"../../DATASET_TEAMS (copy)/elbflorace_labels/", "../../DATASET_TEAMS (copy)/eufs_labels/", "../../DATASET_TEAMS (copy)/fast-forest_labels/",
"../../DATASET_TEAMS (copy)/high-octane_labels/", "../../DATASET_TEAMS (copy)/itu_labels/",
"../../DATASET_TEAMS (copy)/kth_labels/", "../../DATASET_TEAMS (copy)/tallinn_labels/","../../DATASET_TEAMS (copy)/mms_labels/",
"../../DATASET_TEAMS (copy)/scut_labels/", "../../DATASET_TEAMS (copy)/starkstrom_labels/", "../../DATASET_TEAMS (copy)/unicamp_labels/",
"../../DATASET_TEAMS (copy)/vermilion_labels/"] ## Source directory of the labels
 

#SRC_IMG_DIRS = ["../../DATASET_TEAMS (copy)/bme/"]
#SRC_LBLS_DIRS = ["../../DATASET_TEAMS (copy)/bme_labels/"]


## SET NOMENCLATURE
FILE_NAME = "frame" ## Generic name for the files
ZEROS = 8 ## Amount of zeros to fill the generic name: ex. ZEROS = 4 -> 0023

## SET KEY WORDS TO TRANSLATE LABELMAPS
KEY_WORDS = [["yellow", "Yellow", "YELLOW"], ["blue", "Blue", "BLUE"],
             ["orange", "Orange", "ORANGE", "red", "Red"]]

## SET REFERENCE LABEL MAP
REF_LM = "reference_label_map.txt"

## ****************************************************************************************************************
## ****************************************************************************************************************


## DEFINE PATHS
DST_IMAGES = PATH_TO_DST_DATASET_FOLDER + DST_FOLDER_NAME + '/images/'
DST_LABELS = PATH_TO_DST_DATASET_FOLDER + DST_FOLDER_NAME + '/labels/'

DST_IMAGES_TRAIN = DST_IMAGES + 'train/'
DST_IMAGES_VAL = DST_IMAGES + 'val/'
DST_IMAGES_TEST = DST_IMAGES + 'test/'

DST_LABELS_TRAIN = DST_LABELS + 'train/'
DST_LABELS_VAL = DST_LABELS + 'val/'
DST_LABELS_TEST = DST_LABELS + 'test/'

## DEFINE EXTENSIONS
LBS_EXTENSION = "csv" ## Extension of the renamed lbls

## IMPORT REFERENCE LABEL MAP
reference_label_map = load_label_map(REF_LM)


def main():
    ## CHECK PERCENTAGES
    if VAL_PERCENTAGE > 1 or VAL_PERCENTAGE < 0 :
        sys.exit("ENTER A VALID VAL PERCENTAGE VALUE -> IN RANGE [0,1]")

    if TEST_PERCENTAGE > 1 or TEST_PERCENTAGE < 0 :
        sys.exit("ENTER A VALID TEST PERCENTAGE VALUE -> IN RANGE [0,1]")

    if TEST_PERCENTAGE + VAL_PERCENTAGE > 1 :
        sys.exit("ENTER A VALID TEST & VAL PERCENTAGE VALUES -> VAL + TEST + TRAIN = 1")

    ## CHECK ALL FOLDERS ARE CREATED
    if not os.path.exists(PATH_TO_DST_DATASET_FOLDER + DST_FOLDER_NAME):
        os.makedirs(PATH_TO_DST_DATASET_FOLDER + DST_FOLDER_NAME)

    if not os.path.exists(DST_IMAGES):
        os.makedirs(DST_IMAGES)

    if not os.path.exists(DST_LABELS):
        os.makedirs(DST_LABELS)

    if not os.path.exists(DST_IMAGES_TRAIN):
        os.makedirs(DST_IMAGES_TRAIN)

    if not os.path.exists(DST_IMAGES_VAL):
        os.makedirs(DST_IMAGES_VAL)

    if not os.path.exists(DST_IMAGES_TEST):
        os.makedirs(DST_IMAGES_TEST)

    if not os.path.exists(DST_LABELS_TRAIN):
        os.makedirs(DST_LABELS_TRAIN)

    if not os.path.exists(DST_LABELS_VAL):
        os.makedirs(DST_LABELS_VAL)

    if not os.path.exists(DST_LABELS_TEST):
        os.makedirs(DST_LABELS_TEST)

    ## MERGE IMAGES & LABELS
    merged_folders = 0

    for SRC_DIR in SRC_IMG_DIRS:
        ## INFO MSG
        print("MERGING " + SRC_DIR + " ...")

        ## GET LIST OF IMAGES
        src_images = os.listdir(SRC_DIR)
        src_images.sort()
        num_src_files = len(src_images)

        ## GET LIST OF LABELS
        src_labels = os.listdir(SRC_LBLS_DIRS[merged_folders])
        src_labels.sort()

        ## GET LABEL EXTENSION
        labels_extension = src_labels[0][-3:]
        IMG_EXTENSION = src_images[0][-3:] ## Extension of the renamed imgs

        ## GET NUMBER OF IMAGE FOR TEST & VAL
        n_test = round(num_src_files * TEST_PERCENTAGE)
        n_val = round(num_src_files * VAL_PERCENTAGE)

        ## GET VALIDATION FILES
        dst_val_files = os.listdir(DST_IMAGES_VAL)
        num_val_files = len(dst_val_files)

        ## LOAD LABEL MAP
        lm_list = load_label_map(glob.glob(SRC_LBLS_DIRS[merged_folders]+ "label_map*")[0])

        count = 0
        while count < n_val:
            ## CHOOSE RANDOM IMAGE
            img_file = random.choice(src_images)
            label_file = img_file[:-3]+labels_extension

            ## REMOVE FILES FROM LISTS
            src_images.remove(img_file)
            src_labels.remove(label_file)

            ## NEW FILE NAMES
            img_file_rename = FILE_NAME + str(count + num_val_files).zfill(ZEROS) + "." + IMG_EXTENSION
            label_file_rename = FILE_NAME + str(count + num_val_files).zfill(ZEROS) + "." + LBS_EXTENSION

            ## SET NAMES
            old_file = os.path.join(SRC_DIR, img_file)
            new_file = os.path.join(DST_IMAGES_VAL, img_file_rename)

            ## MOVE FILE
            os.rename(old_file, new_file)


            ## CONVERT LABEL TO CSV FORMAT
            convert_label_file(new_file, SRC_LBLS_DIRS[merged_folders]+label_file,
             os.path.join(DST_LABELS_VAL, label_file_rename), reference_label_map, lm_list, KEY_WORDS)

            count += 1

        ## GET TEST FILES
        dst_test_files = os.listdir(DST_IMAGES_TEST)
        num_test_files = len(dst_test_files)

        count = 0
        while count < n_test:
            ## CHOOSE RANDOM IMAGE
            img_file = random.choice(src_images)
            label_file = img_file[:-3]+labels_extension

            ## REMOVE FILES FROM LISTS
            src_images.remove(img_file)
            src_labels.remove(label_file)

            ## NEW FILE NAMES
            img_file_rename = FILE_NAME + str(count + num_test_files).zfill(ZEROS) + "." + IMG_EXTENSION
            label_file_rename = FILE_NAME + str(count + num_val_files).zfill(ZEROS) + "." + LBS_EXTENSION

            ## SET NAMES
            old_file = os.path.join(SRC_DIR, img_file)
            new_file = os.path.join(DST_IMAGES_TEST, img_file_rename)

            ## MOVE FILE
            os.rename(old_file, new_file)

            ## CONVERT LABEL TO CSV FORMAT
            convert_label_file(new_file, SRC_LBLS_DIRS[merged_folders]+label_file,
            os.path.join(DST_LABELS_TEST, label_file_rename), reference_label_map, lm_list, KEY_WORDS)

            count += 1
            
        ## GET TRAIN FILES
        dst_train_files = os.listdir(DST_IMAGES_TRAIN)
        num_train_files = len(dst_train_files)


        count = 0
        for img_file in src_images:
            label_file = img_file[:-3]+labels_extension

            ## NEW FILE NAMES
            img_file_rename = FILE_NAME + str(count + num_train_files).zfill(ZEROS) + "." + IMG_EXTENSION
            label_file_rename = FILE_NAME + str(count + num_train_files).zfill(ZEROS) + "." + LBS_EXTENSION

            ## SET NAMES
            old_file = os.path.join(SRC_DIR, img_file)
            new_file = os.path.join(DST_IMAGES_TRAIN, img_file_rename)

            ## MOVE FILE
            os.rename(old_file, new_file)

            ## CONVERT LABEL TO CSV FORMAT
            convert_label_file(new_file, SRC_LBLS_DIRS[merged_folders]+label_file,
            os.path.join(DST_LABELS_TRAIN, label_file_rename), reference_label_map, lm_list, KEY_WORDS)

            count += 1

        merged_folders += 1

    ## CREATE TRAIN CSV
    merge_csv(DST_IMAGES, DST_LABELS, "train")

    ## CREATE VAL CSV
    merge_csv(DST_IMAGES, DST_LABELS, "val")

    ## CREATE TEST CSV
    merge_csv(DST_IMAGES, DST_LABELS, "test")

    ## TODO: Convert csvs to tfrecords


    final_train_imgs = len(os.listdir(DST_IMAGES_TRAIN))
    final_val_imgs = len(os.listdir(DST_IMAGES_VAL))
    final_test_imgs = len(os.listdir(DST_IMAGES_TEST))

    final_train_labels = len(os.listdir(DST_LABELS_TRAIN))
    final_val_labels = len(os.listdir(DST_LABELS_VAL))
    final_test_labels = len(os.listdir(DST_LABELS_TEST))
    
    print("\n\n")
    print("################################################")
    print("\n")
    print("--- DATASET RESUME ---")
    print("\n")
    print("TRAIN SET : " + str(final_train_imgs) + " images (" + str(final_train_labels) + " labels)")
    print("\n")
    print("VAL SET : " + str(final_val_imgs) + " images (" + str(final_val_labels) + " labels)")
    print("\n")
    print("TEST SET : " + str(final_test_imgs) + " images (" + str(final_test_labels) + " labels)")
    print("\n")
    print("################################################")

if __name__ == "__main__":
    main()