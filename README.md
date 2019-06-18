# Object Localization Dataset Creator
This tool has the aim to help with dataset creation for Object Localization tasks in multiple frameworks.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
```
Write Prerequisites here
```
## Getting this repository
To acquire this repository and start using the tool, please **Fork** the repository using the top right button and then **Clone** the forked repository.

## Contributing
If you want to contribute please read the instructions in [Contribute.md]()

## Using OLDC
### Editing config file
The config file contains all the parameters to modify the tool.

#### Nomenclature
This is the name you will give to the files of the merged dataset it has 2 components:
  - FILE_NAME : Name of the files
  - ZEROS : Number of zeros to complete the file name. This must be set depending on how big your daataset will be.
  ```
  [FILE_NAME = frame] [ZEROS = 8]
  frame00000011
  ```
#### Key Words
Key Words are used to merge datasets which have different label map names to refer to the same objects. 

If no need of translating label maps is required, this field must be an empty array.

**EXAMPLE**

If translation is required:

label map 1 : red-apple green-apple Dog Cat

Our label map : apple dog cat
```
KEY_WORDS = [["apple", "Apple"], ["Dog","dog"], ["Cat","cat"]]
```
If there's no need to translate:
```
KEY_WORDS = []
```

#### Reference Label Map
The reference label map is the label map used in the final dataset and to which all labels are going to be translated.

Path can be edited but it is recomended to use the ones given in the folder **label_maps**

#### Source Directories
Source directories are lists which contain the paths to all folders that need to be merged.

It is important that the first image source directory matches with the first label directory.

IT IS IMPORTANT TO END THE PATH TO DIRECTORIES WITH "/"

**EXAMPLE**

#SRC_IMG_DIRS = ["./path/to/dataset1/images/", "./path/to/dataset2/images/"]

#SRC_LBLS_DIRS = ["./path/to/dataset1/labels/", "./path/to/dataset2/labels/"]

### Creating your dataset
#### Runing OLDC
Once you have set the config file as desired you can create your dataset runing the following command:
```
python create_dataset.py
```

## Check Dataset
To check dataset is well merged, use the cheker.py script:
```
python checker.py
```
