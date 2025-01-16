## Data points to be collected to gain more insights into who is viewing your repository, to better 
## understand the audience and make informed decisions to enhance the repository's 
## content and user experience:
## 1. **IP Address**: The visitor's IP address.
## 2. **Timestamp**: The date and time of the visit.
## 3. **User Agent**: Information about the visitor's browser and operating system.
## 4. **Referrer URL**: The URL from which the visitor came.
## 5. **Requested URL**: The specific URL the visitor is accessing.
## 6. **Geolocation**: Approximate location based on the IP address.
## 7. **Browser and OS**: Detailed information about the visitor's browser and operating system.
## 8. **Screen Resolution**: The visitor's screen resolution.
## 9. **Language**: The preferred language set in the visitor's browser.
## 10. **Session Duration**: The duration of the visitor's session on your site.
## 11. **Page Views**: The number of pages viewed during the session.
## 12. **Device Type**: Whether the visitor is using a desktop, tablet, or mobile device.
## 13. **Query Parameters**: Any query parameters in the URL.
## 14. **Unique Visitor Flag**: A flag to indicate if the visitor is unique.

import os
import datetime
import json
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directory to save logs
log_dir = "_visitors_views_logs"
os.makedirs(log_dir, exist_ok=True)

# Function to get geolocation data based on IP address
def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        return response.json()
    except Exception as e:
        logging.error(f"Error fetching geolocation data: {e}")
        return {}

# Function to collect visitor data (replace with actual data collection)
def collect_visitor_data():
    # Example data, replace with actual data collection logic
    visitor_data = {
        "ip": "192.168.1.1",  # Visitor's IP address
        "timestamp": datetime.datetime.now().isoformat(),  # Timestamp of the visit
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",  # Visitor's browser and OS information (Microsoft Edge)
        "referrer": "https://example.com",  # URL from which the visitor came
        "requested_url": "https://yourrepo.github.io/page",  # URL the visitor is accessing
        "geolocation": get_geolocation("192.168.1.1"),  # Geolocation data based on IP address
        "screen_resolution": "1920x1080",  # Visitor's screen resolution
        "language": "en-US",  # Preferred language set in the visitor's browser
        "session_duration": "5 minutes",  # Duration of the visitor's session
        "page_views": 3,  # Number of pages viewed during the session
        "device_type": "desktop",  # Device type (desktop, tablet, mobile)
        "query_parameters": "param1=value1&param2=value2",  # Query parameters in the URL
        "is_unique": True  # Flag to indicate if the visitor is unique
    }
    return visitor_data

# Function to log visitor data
def log_visitor_data(visitor_data):
    try:
        # Create directories for year and month
        year_dir = os.path.join(log_dir, str(datetime.datetime.now().year))
        month_dir = os.path.join(year_dir, str(datetime.datetime.now().strftime('%Y-%m')))
        os.makedirs(month_dir, exist_ok=True)

        # Log file for the day
        log_file = os.path.join(month_dir, f"{datetime.datetime.now().strftime('%Y-%m-%d')}_visitor_logs.json")

        # Read existing logs
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = json.load(file)
        else:
            logs = []

        # Append new visitor data
        logs.append(visitor_data)

        # Save logs
        with open(log_file, "w") as file:
            json.dump(logs, file, indent=4)

        logging.info("Visitor data logged successfully.")
    except Exception as e:
        logging.error(f"Error logging visitor data: {e}")

# Collect and log visitor data
visitor_data = collect_visitor_data()
log_visitor_data(visitor_data)

# Function to generate summaries for weekly, monthly, quarterly, semi-annual, and annual periods
def generate_summaries():
    try:
        summaries_dir = os.path.join(log_dir, "summaries")
        os.makedirs(summaries_dir, exist_ok=True)

        current_year = datetime.datetime.now().year

        for year in range(current_year - 1, current_year + 1):
            year_dir = os.path.join(log_dir, str(year))
            if not os.path.exists(year_dir):
                continue

            for month in range(1, 13):
                month_str = f"{year}-{month:02d}"
                month_dir = os.path.join(year_dir, month_str)
                if not os.path.exists(month_dir):
                    continue

                monthly_logs = []
                total_count = 0
                for day in range(1, 32):
                    day_str = f"{year}-{month:02d}-{day:02d}"
                    log_file = os.path.join(month_dir, f"{day_str}_visitor_logs.json")
                    if not os.path.exists(log_file):
                        continue

                    with open(log_file, "r") as file:
                        daily_logs = json.load(file)
                        monthly_logs.extend(daily_logs)
                        total_count += len(daily_logs)

                if monthly_logs:
                    monthly_summary_file = os.path.join(summaries_dir, f"{month_str}_summary.json")
                    summary_data = {
                        "total_count": total_count,
                        "logs": monthly_logs
                    }
                    with open(monthly_summary_file, "w") as file:
                        json.dump(summary_data, file, indent=4)

                    logging.info(f"Monthly summary generated for {month_str} with total count {total_count}")
    except Exception as e:
        logging.error(f"Error generating summaries: {e}")

# Generate summaries
generate_summaries()
