import os

def delete_files_with_size(directory, file_size_in_bytes):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and os.path.getsize(filepath) == file_size_in_bytes: #here
            os.remove(filepath)
            print(f"Deleted: {filepath}")

directory_path = "" # Put the folder path here
file_size_in_bytes = 503 # Change your reapeted size of the images, in my case the reapeted file size is 503 bytes 
delete_files_with_size(directory_path, file_size_in_bytes)
