import requests
import os

def download_image(url, file_name):
  response = requests.get(url)
  open(file_name, "wb").write(response.content)

# Replace "SEARCH_QUERY" with the search query you want to use
search_query = "SEARCH_QUERY"

# Replace "DIRECTORY_NAME" with the name of the directory you want to save the images to
directory_name = "DIRECTORY_NAME"

# Make sure the directory exists
if not os.path.exists(directory_name):
  os.makedirs(directory_name)

# Set the maximum number of images you want to download
max_images = 100

# Set the starting value for the image number
image_number = 1

# Set the URL for the Google Image Search API
url = "https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_SEARCH_ENGINE_ID&q=" + search_query + "&searchType=image&start=" + str(image_number)

# Send a request to the Google Image Search API
response = requests.get(url).json()

# Iterate through the results and download each image
for item in response["items"]:
  image_url = item["link"]
  file_name = directory_name + "/" + str(image_number) + ".jpg"
  download_image(image_url, file_name)
  image_number += 1
  if image_number > max_images:
    break
