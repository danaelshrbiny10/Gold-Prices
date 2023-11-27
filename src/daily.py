# This script is used for scraping gold prices in Egypt.
# It makes an API request to `https://pricegold.net/eg-egypt/` using the provided API key.
# The data obtained includes today's updated gold prices in Egypt.
# If the response is in valid JSON format, it is parsed and printed.
# If the response is not valid JSON, an error message is displayed.

# Helpful Links:
# - Documentation on web scraping in Python: https://python-adv-web-apps.readthedocs.io/en/latest/scraping.html
# - Documentation for the 'requests' library: https://requests.readthedocs.io/en/latest/
# - Free Gold Price API: https://goldpricez.com/about/api


from datetime import datetime
import json
import requests

url: str = "https://pricegold.net/eg-egypt/"

live_url: str = "https://pricegold.net/ajax.php?do=live"

api_key: str = "2727145611bbd2e6b3fde2eaf3d25d8227271456"

headers: dict = {"Authorization": f"Bearer {api_key}"}

# Send an HTTP GET request to the API
response = requests.get(url, headers=headers)

# list to store the enhanced data for live
enhanced_live_data = []


if response.status_code == 200:
    """Check if the response status code is 200 (OK)."""
    try:
        """Parse the JSON response."""
        data = response.json()
        print(data)

        with open("daily_local.json", "w", encoding="utf-8") as json_file:
            """Save the JSON data to a file with UTF-8 encoding."""
            json_file.write(json.dumps(data, ensure_ascii=False, indent=4))

    except ValueError:
        """Handle JSON parsing errors."""
        response_text = response.text

        with open("data/scraping/daily_local.csv", "w", encoding="utf-8") as csv_file:
            """If the response is not valid JSON, save it as CSV with UTF-8 encoding."""
            csv_file.write(response_text)
        print(f"Response saved as CSV: daily_local.csv")

else:
    """Handle non-200 status codes."""
    print(f"Failed to retrieve HTML. Status code: {response.status_code}")

