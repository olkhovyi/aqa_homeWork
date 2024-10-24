import requests
import os

# Uploading an image via a POST request
url_upload = "http://127.0.0.1:8080/upload"
image_path = os.path.join(os.getcwd(), 'image1.jpg')
if os.path.exists(image_path):
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(url_upload, files=files)
        if response.status_code == 201:
            image_url = response.json().get('image_url')
            print(f"Image uploaded at: {image_url}")
        else:
            print(f"Download error: {response.status_code} - {response.text}")
else:
    print(f"Image file '{image_path}' not found")

# Getting the image URL via a GET request
if image_url:
    filename = image_url.split('/')[-1]
    url_get_image = f"http://127.0.0.1:8080/uploads/{filename}"

    # Set the Content-Type: text header to get the URL
    headers = {'Content-Type': 'text'}
    response = requests.get(url_get_image, headers=headers)
    if response.status_code == 200:
        print(f"Image available at URL: {response.json().get("image_url")}")
    else:
        print(f"Error getting image: {response.status_code} - {response.text}")

# Deleting an image via a DELETE request
if image_url:
    url_delete_image = f"http://127.0.0.1:8080/delete/{filename}"
    response = requests.delete(url_delete_image)
    if response.status_code == 200:
        print(f"Image removed: {response.json()['message']}")
    else:
        print(f"Error deleting image: {response.status_code} - {response.text}")

