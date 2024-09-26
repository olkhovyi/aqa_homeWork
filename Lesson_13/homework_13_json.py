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
            json_data = response.json()  # Trying to convert to JSON
        except json.JSONDecodeError as e:
            logging.error(f"Невалідний JSON файл за URL: {url}. Помилка: {e}")
            print(f"Невалідний JSON файл: {url}")
        except requests.RequestException as e:
            logging.error(f"Не вдалося завантажити файл з {url}. Помилка: {e}")
            print(f"Не вдалося завантажити файл: {url}")

validate_json_from_urls(json_urls)

