import requests

# URL NASA API
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
response = requests.get(url, params=params)

# Check the status of the response
if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if photos:
        # Let's upload the first few photos
        for idx, photo in enumerate(photos[:5], start=1):
            img_url = photo['img_src']
            print(f"Uploading a photo {idx}: {img_url}")

            # Image download request
            img_response = requests.get(img_url)

            # Check the status of the response
            if img_response.status_code == 200:
                img_filename = f"mars_photo{idx}.jpg"

                # Save the photo to the current directory
                with open(img_filename, 'wb') as file:
                    file.write(img_response.content)

                print(f"Photo {idx} saved as {img_filename}")
            else:
                print(f"Failed to upload photo {idx}")
    else:
        print("No photo found to upload.")
else:
    print(f"An error occurred while requesting the NASA API: {response.status_code}")
