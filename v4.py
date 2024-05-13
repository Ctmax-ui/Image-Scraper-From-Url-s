import os
import asyncio
import aiohttp
import aiofiles

async def download_image(session, url, save_folder, retries=3):
    for attempt in range(retries):
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
                    break  # Break out of retry loop if successful
                else:
                    print(f"Failed to download image from {url}: {response.status}")
        except aiohttp.ClientError as ce:
            print(f"Error downloading image from {url}: {ce}")
        except asyncio.TimeoutError as te:
            print(f"Timeout error downloading image from {url}: {te}")
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
            continue  # Retry the download
        except Exception as e:
            print(f"Unhandled error downloading image from {url}: {e}")

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

    # Limit concurrent requests using semaphore
    semaphore = asyncio.Semaphore(10)  # Limit to 10 concurrent requests

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as session:
        tasks = [download_image(session, url.strip(), save_folder) for url in urls]
        await asyncio.gather(*tasks, return_exceptions=True)

# Run the download_images_from_urls function
asyncio.run(download_images_from_urls())
