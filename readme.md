# Image Scraper From bunch of url text file.

## Introduction
This guide provides step-by-step instructions for utilizing a Python script to scrape images from a URL list and remove duplicate or unwanted images from a specified folder.

## Setup Instructions

1. **Download or Clone Repository**: Begin by downloading or cloning the Git repository containing the necessary scripts.

2. **Open `run_scraper.py`**: Using a text editor like Notepad or any other preferred text editor, open the `run_scraper.py` file.

3. **Adjust URL File Path**:
   - Navigate to the end of the code in `run_scraper.py`.
   - Locate the variable `url_file_path = ''`.
   - Set the value of `url_file_path = 'urls/example_url.txt'` to the path of the text file containing the URLs of the images to be scraped.

4. **Specify Save Folder**:
   - Below the `url_file_path`, find the variable `save_folder`.
   - Set the value of `save_folder= 'images/example_image'` to the desired path where you want to save the scraped images.

5. **Run Scraper Multiple Times**:
   - It's recommended to run the scraper multiple times to ensure all images are captured and not missed.

6. **Adjust Duplicate Image Removal**:
   - Open the `del.py` file in your preferred text editor.
   - Locate the variable `directory_path = 'images/example_image'` and set it to the folder containing the images you want to remove duplicates from.
   - Specify the size of images to identify duplicates using `file_size_in_bytes = 503`. In bytes

7. **Execute Duplicate Removal Script**:
   - Run the command `python3 del.py` to execute the script for removing duplicate or unwanted images.

8. **Info about v4.py and v5-del.py**
   - Run those so you do not have to go through hassel of modifying every time you change your urls path and the save folder path.

9. **Ifor abour topng.py**
   - Run `Python3 topng.py` this if your image download in other format like example_img.doc or example_img(w/o any format) or any kind of extension it will convert all the images into (.png) type, so you do not have to go through naming them.

## Important Note
Use this code at your own risk. The creator of this code shall not be held liable for any consequences resulting from its use.

---

*Note: Ensure you have Python installed on your system to execute the scripts.
    Also install this pip `pip install asyncio`, `pip install aiohttp`, `pip install aiofiles`, `pip install os`*
