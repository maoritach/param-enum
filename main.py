import requests
import json
import argparse
import sys
from tabulate import tabulate

# ANSI escape sequences for colors
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# Function to select the cluster
def select_cluster():
    clusters = {"1": "eu.brightsec.com", "2": "app.brightsec.com"}
    while True:
        print("Choose a cluster:")
        for key, value in clusters.items():
            print(f"[{key}] {value}")
        selection = input("Enter your choice (1 or 2): ")
        if selection in clusters:
            return clusters[selection]
        else:
            print("Invalid selection. Please choose 1 or 2.")

# Function to run the interactive wizard
def run_wizard():
    project_id = input("Enter Project ID: ")
    discovery_id = input("Enter Discovery ID: ")
    key = input("Enter Project API Key: ")
    base_url = select_cluster()
    return project_id, discovery_id, key, base_url

# Set up the argument parser
parser = argparse.ArgumentParser(description="API Request Script")
parser.add_argument('-p', '--project', help='Project ID')
parser.add_argument('-d', '--discovery', help='Discovery ID')
parser.add_argument('-t', '--api-key', help='API Key')
parser.add_argument('-c', '--cluster', choices=['eu', 'app'], help='Cluster (eu or app)')

# Parse the arguments
args = parser.parse_args()

# Check if any arguments were provided
if len(sys.argv) == 1:
    # No arguments, run the interactive wizard
    project_id, discovery_id, key, base_url = run_wizard()
else:
    # Arguments provided, use them
    project_id = args.project
    discovery_id = args.discovery
    key = args.api_key
    if args.cluster == "eu":
        base_url = "eu.brightsec.com"
    elif args.cluster == "app":
        base_url = "app.brightsec.com"
    else:
        base_url = select_cluster()  # Default to interactive cluster selection if no cluster argument

# Form the URL
url = f"https://{base_url}/api/v2/projects/{project_id}/discoveries/{discovery_id}/sitemap"

headers = {
    "Authorization": f"api-key {key}",
    "Content-Type": "application/json"
}

# Make the GET request to the API
response = requests.get(url, headers=headers)

# If the response was successful, no Exception will be raised
response.raise_for_status()

# Parse the JSON response
data = response.json()
# Convert the entire JSON response to a string
response_text = json.dumps(data)

# Define the specific patterns to check
patterns = ['"name": "body"', '"name": "query"', '"name": "path"', '"name": "fragment"', '"name": "header"', '"name": "artificalfragment"', '"name": "artificalquery"']

# Check for each pattern and store results in a list for the table
results = []
for pattern in patterns:
    param_type = pattern.split('"')[3]
    if pattern in response_text:
        results.append([param_type.capitalize() + " parameters", GREEN + "Yes" + ENDC])
    else:
        results.append([param_type.capitalize() + " parameters", RED + "No" + ENDC])

# Print the results in a table
print(tabulate(results, headers=["Parameter", "Found"], tablefmt="rounded_outline"))





