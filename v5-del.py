import os
import asyncio
import aiohttp
import aiofiles

async def download_image(session, url, save_folder):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                # Extract image file name from URL
                image_name = os.path.basename(url)
                # Save the image to the specified folder
                image_path = os.path.join(save_folder, image_name)
                if not os.path.exists(image_path):
                    async with aiofiles.open(image_path, 'wb') as image_file:
                        await image_file.write(await response.read())
                    print(f"Downloaded image: {image_name}")
                else:
                    print(f"Image already exists: {image_name}")
            else:
                print(f"Failed to download image from {url}: {response.status}")
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")

async def download_images_from_urls():
    # Prompt the user for URL file path and save folder
    url_file_path = input("Enter the path to the text file containing image URLs: ")
    save_folder = input("Enter the folder to save downloaded images: ")

    # Create the save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Read URLs from the text file
    with open(url_file_path, 'r') as file:
        urls = file.readlines()

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url.strip(), save_folder) for url in urls]
        await asyncio.gather(*tasks)

    # Delete files with size 503 bytes after downloading all images
    delete_files_with_size(save_folder)

def delete_files_with_size(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if the file size is 503 bytes
        if os.path.isfile(filepath) and os.path.getsize(filepath) == 503:
            # Delete the file
            os.remove(filepath)
            print(f"Deleted: {filepath}")

# Run the download_images_from_urls function
asyncio.run(download_images_from_urls())
