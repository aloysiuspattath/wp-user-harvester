#!/usr/bin/env python

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import re

# Function to validate URL
def is_valid_url(url):
    # Basic URL validation using regex
    return re.match(r'^https?://[^\s/$.?#].[^\s]*$', url) is not None

# Function to validate if a string is a number
def is_number(value):
    return value.isdigit()

# Function to print the custom ASCII art for the script name
def print_ascii_art():
    ascii_art = r"""
                                        _                              _            
                                       | |                            | |           
__      ___ __    _   _ ___  ___ _ __  | |__   __ _ _ ____   _____ ___| |_ ___ _ __ 
\ \ /\ / | '_ \  | | | / __|/ _ | '__| | '_ \ / _` | '__\ \ / / _ / __| __/ _ | '__|
 \ V  V /| |_) | | |_| \__ |  __| |    | | | | (_| | |   \ V |  __\__ | ||  __| |   
  \_/\_/ | .__/   \__,_|___/\___|_|    |_| |_|\__,_|_|    \_/ \___|___/\__\___|_|   
         | |                                                                        
         |_|                                                                        
   
    Ver: 1.0                                               by: Aloysius Pattath
    """
    print(ascii_art)
    
    
# Function to check and retrieve data from different WordPress API endpoints
def fetch_wordpress_data(site_url, num_range=5):
    if not is_valid_url(site_url):
        print("Invalid URL provided.")
        return

    # List of API endpoints to check
    endpoints = [
        f"{site_url}/wp-json/wp/v2/users",
        f"{site_url}/wp-json/?rest_route=/wp/v2/users",
        f"{site_url}/wp-json/tenwebio/v2/compress-one",
        f"{site_url}/wp-json/oembed/1.0/embed?url={site_url}&format=json",
    ]

    # Add numeric variations for endpoints that require numeric ID (n)
    for n in range(1, num_range + 1):  # You can adjust num_range to check more numbers
        endpoints += [
            f"{site_url}/wp-json/wp/v2/users/{n}",
            f"{site_url}/wp-json/?rest_route=/wp/v2/users/{n}",
            f"{site_url}/wp-json/wp/v2/sensei-messages/{n}",
            f"{site_url}/?author={n}",
        ]

    users = {}  # Dictionary to store user data, keyed by user_id

    # Initialize the progress bar
    with tqdm(total=len(endpoints), desc="Fetching data", unit="endpoint") as pbar:
        # Iterate through all the generated endpoints
        for endpoint in endpoints:
            try:
                response = requests.get(endpoint)

                # Check if the request was successful
                if response.status_code == 200:
                    # Check if the URL returns JSON
                    try:
                        data = response.json()
                        if isinstance(data, list):
                            for user in data:
                                add_user(user, users)
                        elif isinstance(data, dict):
                            add_user(data, users)
                    except ValueError:
                        # Not JSON, handle as HTML or other content
                        print(f"Non-JSON response from {endpoint}. Parsing HTML...")
                        if '/?author=' in endpoint:
                            fetch_and_parse_author_page(endpoint, users)
                elif response.status_code == 404:
                    print(f"Endpoint not found: {endpoint}")
                else:
                    print(f"Failed to retrieve data from {endpoint}. Status code: {response.status_code}")

            except requests.RequestException as e:
                print(f"Error occurred while accessing {endpoint}: {e}")
            
            # Update the progress bar
            pbar.update(1)

    # Display the final results in a readable format
    print("\nFinal Results (unique users):")
    for user_id, user_info in users.items():
        print(f"User ID: {user_id}, Username: {user_info['username']}, Display Name: {user_info['display_name']}")

# Function to add user data to the users dictionary, avoiding duplicates
def add_user(user, users):
    user_id = user.get('id')
    if user_id and user_id not in users:
        users[user_id] = {
            'username': user.get('name', 'N/A'),
            'display_name': user.get('display_name', 'N/A')
        }

# Function to fetch and parse user data from /?author=n pages
def fetch_and_parse_author_page(url, users):
    try:
        # Follow redirects
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 200:
            # Fetch the final redirected URL
            final_url = response.url
            print(f"Redirected to: {final_url}")

            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract author name and user details
            username_tag = soup.find('meta', property='og:title')  # Example tag, adjust as needed
            if username_tag:
                user_name_text = username_tag['content']
                author_id = extract_author_id(final_url)
                if author_id:
                    users[author_id] = {'username': user_name_text, 'display_name': user_name_text}
        else:
            print(f"Failed to retrieve author page from {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error occurred while accessing {url}: {e}")

# Function to extract author ID from the URL (simplified assumption)
def extract_author_id(url):
    # Extract numeric ID from URL (after '/author/')
    parts = url.rstrip('/').split('/')
    if len(parts) > 2 and parts[-2] == 'author':
        return parts[-1]
    return None

# Function to get the site URL from the user and call fetch_wordpress_data
def main():
    print_ascii_art()
    site_url = input("Enter the WordPress site URL (without trailing slash, e.g., https://example.com): ").strip()
    
    if not is_valid_url(site_url):
        print("Invalid URL. Please enter a valid URL.")
        return

    num_range_input = input("Enter the range of numbers to check for iterable endpoints (e.g., 5 for checking up to 5): ").strip()
    
    if not is_number(num_range_input):
        print("Invalid number. Please enter a valid number.")
        return

    num_range = int(num_range_input)
    fetch_wordpress_data(site_url, num_range)

if __name__ == "__main__":
    main()
