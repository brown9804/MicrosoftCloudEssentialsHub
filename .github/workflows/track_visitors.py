## Data points to be collected to gain more insights into who is viewing your repository, to better 
## understand the audience and make informed decisions to enhance the repository's 
## content and user experience:
## 1. **Timestamp**: The date and time of the visit.
## 2. **User Agent**: Information about the visitor's browser and operating system.
## 3. **Referrer URL**: The URL from which the visitor came.
## 4. **Requested URL**: The specific URL the visitor is accessing.
## 5. **Page Views**: The number of pages viewed during the session.
## 6. **Unique Visitor Flag**: A flag to indicate if the visitor is unique.

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

# Function to fetch traffic data from GitHub API
def fetch_traffic_data(repo):
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/repos/{repo}/traffic/views"
    response = requests.get(url, headers=headers)
    return response.json()

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

        # Summarize the time and pages viewed for the same person
        summary = {
            "total_visitors": len(logs),
            "unique_visitors": len(set((log["timestamp"], log["user_agent"]) for log in logs)),
            "total_page_views": sum(log["count"] for log in logs)
        }
        
        with open(log_file, "w") as file:
            json.dump({"summary": summary, "logs": logs}, file, indent=4)

        logging.info("Visitor data logged successfully.")
    except Exception as e:
        logging.error(f"Error logging visitor data: {e}")

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
                unique_visitors = {}
                daily_counts = {}
                for day in range(1, 32):
                    day_str = f"{year}-{month:02d}-{day:02d}"
                    log_file = os.path.join(month_dir, f"{day_str}_visitor_logs.json")
                    if not os.path.exists(log_file):
                        continue

                    with open(log_file, "r") as file:
                        daily_logs = json.load(file)
                        monthly_logs.extend(daily_logs)
                        total_count += len(daily_logs)
                        daily_counts[day_str] = len(daily_logs)

                        for log in daily_logs:
                            key = (log["timestamp"], log["user_agent"])
                            if key not in unique_visitors:
                                unique_visitors[key] = {
                                    "page_views": log["count"],
                                    "count": 1,
                                }
                            else:
                                unique_visitors[key]["page_views"] += log["count"]
                                unique_visitors[key]["count"] += 1

                if monthly_logs:
                    monthly_summary_file = os.path.join(summaries_dir, f"{month_str}_summary.json")
                    summary_data = {
                        "total_count": total_count,
                        "daily_counts": daily_counts,
                        "unique_visitors": unique_visitors,
                        "logs": monthly_logs,
                    }
                    with open(monthly_summary_file, "w") as file:
                        json.dump(summary_data, file, indent=4)

                    logging.info(f"Monthly summary generated for {month_str} with total count {total_count}")
    except Exception as e:
        logging.error(f"Error generating summaries: {e}")

# Main function to run the script
def main():
    repo_name = os.getenv('REPO_NAME', 'brown9804/MicrosoftCloudEssentialsHub')  # Replace with your default repository name or set it dynamically using environment variable
    traffic_data = fetch_traffic_data(repo_name)
    log_visitor_data(traffic_data)
    generate_summaries()

if __name__ == "__main__":
    main()
