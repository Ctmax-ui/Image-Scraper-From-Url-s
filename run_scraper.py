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

async def download_images_from_urls(url_file_path, save_folder):
    # Create the save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Read URLs from the text file
    with open(url_file_path, 'r') as file:
        urls = file.readlines()

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url.strip(), save_folder) for url in urls]
        await asyncio.gather(*tasks)

url_file_path = ''+'.txt'  # Path to the text file containing image URLs
save_folder = ''      # Folder to save downloaded images

asyncio.run(download_images_from_urls(url_file_path, save_folder))
