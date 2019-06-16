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
Key Words are used to merge datasets which have different label map names to refer to the same objects. If no need of translating label maps is required, this field must be an empty array.

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
