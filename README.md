# TwitterV2

## Overview

TwitterV2 is a Python application that searches for a Twitter user and retrieves their tweets. The app uses web scraping techniques to extract tweet information and display it in the console.

## Python Libraries Used

- BeautifulSoup
- requests
- PIL (Python Imaging Library)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/abqareno/TwitterV2.git
   ```
2. Navigate to the project directory:
   ```
   cd TwitterV2
   ```
3. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python main.py
   ```

## Code Files

### `main.py`

Contains the main functionality to search for a Twitter user and display their tweets. It uses the `BeautifulSoup` library to parse the HTML content of the Twitter page and extract tweet information. The `requests` library is used to make HTTP requests to the Twitter website. The `PIL` library is used to handle images in tweets.

### `Classes/formatting.py`

Contains a class for text formatting with colors. The `color` class defines various color codes that can be used to format text output in the console.

## Usage Instructions

1. Run the application by executing the `main.py` file:
   ```
   python main.py
   ```
2. Enter the Twitter username you want to search for when prompted.
3. The application will display the tweets of the specified user in the console, along with any images found in the tweets.
