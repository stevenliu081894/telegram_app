from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import cloudscraper

# Set up headless browser options
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--no-sandbox")  # Some AWS instances need this flag
options.add_argument("--disable-dev-shm-usage")  # Required for running in Docker/AWS

# Set up the WebDriver service using ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# URL you want to scrape
URL = "https://feed.bithumb.com/notice"

# Open the URL
driver.get(URL)

# Wait for the page to load completely
time.sleep(3)  # Adjust wait time if needed (or use WebDriverWait for better handling)

# Get cookies
cookies = driver.get_cookies()
print(f"Cookies: {cookies}")
# Add cookies manually to your WebDriver session
# Get all cookies from the current session

# Close the driver after extracting cookies
driver.quit()

# Convert cookies to a format that cloudscraper can use
cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}

# Now use cloudscraper with the extracted cookies

 # Set up headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}
scraper = cloudscraper.create_scraper()

# Set the cookies
scraper.cookies.update(cookie_dict)

# Make the request using the cookies
response = scraper.get(URL, headers=headers)

# Output the response text
print(response.text)