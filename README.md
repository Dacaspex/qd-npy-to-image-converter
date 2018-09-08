# qd-npy-to-image-converter
Converts Google's "Quick, Draw!" .npy files to images

## Summary
This python script converts the `.npy` data from the [dataset](https://github.com/googlecreativelab/quickdraw-dataset) from the "Quick, Draw!" game made by Google into images. It takes the `.npy` file from the `data/` folder and outputs the images into the `output/` folder.

## Install instructions
### Windows
1. Clone this repository  
  ```
  git clone https://github.com/googlecreativelab/quickdraw-dataset
  ```
2. Create a virtual environment  
  ```
  python -m venv <directory>
  ```
3. CD into the directory and start the environmet
  ```
  Scripts\activate.bat
  ```
4. Install packages from `requirements.txt` with pip
  ```
  pip install -r requirements.txt
  ```
5. Run program
  ```
  python import.py
  ```
