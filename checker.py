import cv2
import sys
import csv
import os

dataset_name = "MERGED_MUNICH_DATASET"

def main():
  while 1:
    txt = input("\nq to exit otherwhise path\n")
    if txt == 'q' or txt == 'Q':
      sys.exit()
    else:
      ## Open Image
      if not os.path.isfile(txt):
        print("FILE DOES NOT EXIST")
        continue
      elif txt[-3:] is 'jpg' or txt[-3:] is 'png':
        print("THIS FILE IS NOT AN IMAGE")
        continue
      else:
        img = cv2.imread(txt)
        img_ext = txt[-3:]
        label_path = txt.replace(img_ext, "csv")
        label_path = label_path.replace("images", "labels")

        with open(label_path, 'r') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              print(row['ymin'])
              cv2.rectangle(img, (int(row['xmin']), int(row['ymin'])), (int(row['xmax']), int(row['ymax'])), (255,0,0), 2)
          
        cv2.imshow("CHECK", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
          
if __name__ == "__main__":
  main()

