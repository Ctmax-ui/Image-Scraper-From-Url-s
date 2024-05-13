import os

def rename_to_png(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is not already in PNG format
        if not filename.lower().endswith('.png'):
            # Construct the new filename with the PNG extension
            new_filename = os.path.splitext(filename)[0] + '.png'
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Provide the correct directory path where your files are located
directory_path = ''
rename_to_png(directory_path)
