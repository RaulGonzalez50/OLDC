import cv2
import numpy as np
import sys
import csv
import os
from utils.utils import load_label_map
dataset_name = "MERGED_MUNICH_DATASET"

def main():
  lm = load_label_map("reference_label_map.txt")
  print(lm)
  labels_color = []
  for _ in lm:
     labels_color.append(list(np.random.choice(range(256), size=3)))
  print(labels_color)
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
              print(labels_color[lm.index(str(row['class']))])
              cv2.rectangle(img, (int(row['xmin']), int(row['ymin'])), (int(row['xmax']), int(row['ymax'])), labels_color[lm.index(str(row['class']))], 2)
              cv2.putText(img,str(row['class']),(int(row['xmax'])+10,int(row['ymax'])), 0, 0.3, labels_color[lm.index(str(row['class']))])
          
        cv2.imshow("CHECK", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
          
if __name__ == "__main__":
  main()

