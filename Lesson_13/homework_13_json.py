import requests
import json
import logging


logging.basicConfig(filename='json_olkhovyi.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# List of URLs of JSON files from GitHub
json_urls = [
    "https://github.com/dntpanix/automation_qa/blob/0c61017dfea127e5e4a048bfc411f07e1c324b27/ideas_for_test/work_with_json/localizations_en.json",
    "https://github.com/dntpanix/automation_qa/blob/0c61017dfea127e5e4a048bfc411f07e1c324b27/ideas_for_test/work_with_json/localizations_ru.json",
    "https://github.com/dntpanix/automation_qa/blob/0c61017dfea127e5e4a048bfc411f07e1c324b27/ideas_for_test/work_with_json/login.json",
    "https://github.com/dntpanix/automation_qa/blob/0c61017dfea127e5e4a048bfc411f07e1c324b27/ideas_for_test/work_with_json/swagger.json"
]

# A function to check the validity of JSON files from URL
def validate_json_from_urls(json_urls):
    for url in json_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # We check whether the file was successfully downloaded

            # Try to load the JSON to validate its correctness
            json.loads(response.text)
            print(f"File at URL {url} is valid.")

        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON file for URL: {url}. Error: {e}")
            print(f"Invalid JSON file: {url}")
        except requests.RequestException as e:
            logging.error(f"Failed to download file from {url}. Error: {e}")
            print(f"Failed to download file: {url}")

validate_json_from_urls(json_urls)

