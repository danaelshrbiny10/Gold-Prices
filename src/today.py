# This script is used for scraping gold prices in Egypt today.
# It makes an API request to `https://pricegold.net/eg-egypt/` using the provided API key.
# The data obtained includes today's updated gold prices in Egypt.
# If the response is in valid JSON format, it is parsed and printed.
# If the response is not valid JSON, an error message is displayed.

# Helpful Links:
# - Documentation on web scraping in Python: https://python-adv-web-apps.readthedocs.io/en/latest/scraping.html
# - Documentation for the 'requests' library: https://requests.readthedocs.io/en/latest/
# - Documentation for the 'Json' library: https://docs.python.org/3/library/json.html
# - Free Gold Price API: https://goldpricez.com/about/api

import csv
from datetime import datetime
import json
import os
import requests


today_url: str = "https://pricegold.net/ajax.php?do=today"

api_key: str = "2727145611bbd2e6b3fde2eaf3d25d8227271456"

headers: dict = {"Authorization": f"Bearer {api_key}"}

# Send an HTTP GET request to the API
response = requests.get(today_url, headers=headers)


if response.status_code == 200:
    """Parse the JSON response."""
    data = response.json()

    # list to store the enhanced data for today
    enhanced_today_data = []

    for timestamp, price in data:
        """Convert the timestamp from milliseconds to seconds."""
        timestamp_seconds = timestamp / 1000

        # Convert the timestamp to a human-readable date string.
        date_str = datetime.fromtimestamp(timestamp_seconds).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Round the price to a specified number of decimal places (e.g., 2 decimal places)
        rounded_price = round(price, 2)

        # Create an enhanced data entry with the timestamp in a readable format and the formatted price
        enhanced_entry = {"Timestamp": date_str, "Price": rounded_price}

        enhanced_today_data.append(enhanced_entry)

    directory = "data/scraping"
    os.makedirs(directory, exist_ok=True)
    csv_file_name = os.path.join(directory, "gold_today.csv")

    # Save the data to a CSV file in the specified directory
    with open(csv_file_name, mode="w", newline="") as csv_file:
        fieldnames = ["Timestamp", "Price"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for entry in enhanced_today_data:
            writer.writerow(entry)

    # enhanced_today_data contains the enhanced JSON data
    print(json.dumps(enhanced_today_data, indent=4))
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
