In that case, let's update the `README.md` to reflect that you're using `setup.py` instead of `requirements.txt`. Here’s the revised `README.md`:

---

# WP User Harvester

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.7%2B-green)
![License](https://img.shields.io/badge/license-MIT-green)

`WP User Harvester` is a Python tool designed to gather user data from WordPress websites using various API endpoints and URL iteration (e.g., `/?author=n`). The tool fetches user details such as usernames, display names, and more by interacting with the WordPress REST API.

## Features
- Validates WordPress URLs before scraping.
- Fetches user details from multiple WordPress REST API endpoints.
- Supports iteration over user IDs (e.g., `/?author=n`).
- Displays real-time progress using a progress bar (powered by `tqdm`).
- User-friendly command-line interface.

## ASCII Art

```
                                        _                              _            
                                       | |                            | |           
__      ___ __    _   _ ___  ___ _ __  | |__   __ _ _ ____   _____ ___| |_ ___ _ __ 
\ \ /\ / | '_ \  | | | / __|/ _ | '__| | '_ \ / _` | '__\ \ / / _ / __| __/ _ | '__|
 \ V  V /| |_) | | |_| \__ |  __| |    | | | | (_| | |   \ V |  __\__ | ||  __| |   
  \_/\_/ | .__/   \__,_|___/\___|_|    |_| |_|\__,_|_|    \_/ \___|___/\__\___|_|   
         | |                                                                        
         |_|                                                                        
   
    Ver: 1.0                                               by: Aloysius Pattath
```

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/aloysiuspattath/wp-user-harvester.git
cd wp-user-harvester
```

### Step 2: Set Up Virtual Environment (optional, but recommended)
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### Step 3: Install Dependencies using `setup.py`
```bash
pip install .
```

This command will install all the required libraries as listed in the `setup.py` file.

### Step 4: Run the Script
```bash
python wp_user_harvester.py
```

## Usage

### Command-Line Interface
1. Run the script:
    ```bash
    python wp_user_harvester.py
    ```

2. Input the WordPress site URL (without a trailing slash). Example:
    ```
    Enter the WordPress site URL (without trailing slash, e.g., https://example.com): https://example.com
    ```

3. Input the range of numbers to iterate over user IDs:
    ```
    Enter the range of numbers to check for iterable endpoints (e.g., 5 for checking up to 5): 5
    ```

The tool will display a progress bar while fetching data and will show the final list of unique users retrieved from the WordPress site.

### Example Output
```bash
Fetching data: 100%|███████████████████████████████████████████████████████████████████████████████████| 12/12 [00:13<00:00,  1.09s/endpoint]

Final Results (unique users):
User ID: 1, Username: admin, Display Name: Admin User
User ID: 2, Username: editor, Display Name: Editor User
```

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Open a pull request.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---
