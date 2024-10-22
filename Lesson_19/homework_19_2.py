import requests

# Uploading an image via a POST request
url_upload = "http://127.0.0.1:8080/upload"
image_path = "C:\Image\image1.png"
with open(image_path, 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post(url_upload, files=files)
    if response.status_code == 201:
        image_url = response.json()['image_url']
        print(f"Image uploaded at: {image_url}")
    else:
        print(f"Download error: {response.status_code}")

# Getting the image URL via a GET request
filename = image_url.split('/')[-1]
url_get_image = f"http://127.0.0.1:8080/image/{filename}"
response = requests.get(url_get_image)
if response.status_code == 200:
    print(f"Image available at URL: {url_get_image}")
else:
    print(f"Error getting image: {response.status_code}")

# Deleting an image via a DELETE request
url_delete_image = f"http://127.0.0.1:8080/delete/{filename}"
response = requests.delete(url_delete_image)
if response.status_code == 200:
    print(f"Image removed: {response.json()['message']}")
else:
    print(f"Error deleting image: {response.status_code}")
