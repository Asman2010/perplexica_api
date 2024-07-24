import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.exceptions import RequestException
from typing import Tuple

class InternetSearch:
    BASE_URL = "http://localhost:3000"
    API_URL = "http://localhost:3001/api/chats/"
    WAIT_TIME = 10 # Reduced wait time
    MAX_RETRIES = 6  # Maximum number of retries

    def __init__(self, query: str):
        self.query = query
        self.driver = None

    def format_query(self) -> str:
        return self.query.replace(" ", "+")

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def search(self):
        self.setup_driver()
        try:
            url = f"{self.BASE_URL}/?q={self.format_query()}&format=json"
            print(f"Navigating to: {url}")
            self.driver.get(url)
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".response-content"))
            )
            print("Search completed successfully")
        except Exception as e:
            print(f"An error occurred during the search: {e}")
        finally:
            self.driver.quit()

    def fetch_id(self) -> Tuple[str, str]:
        try:
            response = requests.get(self.API_URL, timeout=5)
            response.raise_for_status()
            recent_chat = response.json()["chats"][0]
            return recent_chat["id"], recent_chat["title"]
        except (RequestException, KeyError, IndexError) as e:
            print(f"Error fetching chat ID: {e}")
            return None, None

    def check(self) -> str:
        for _ in range(self.MAX_RETRIES):
            chat_id, chat_query = self.fetch_id()
            if chat_query == self.query:
                return chat_id
            time.sleep(self.WAIT_TIME)
        raise TimeoutError("Max retries reached. Chat not found.")

    def process(self) -> str:
        try:
            chat_id = self.check()
            url = f"{self.API_URL}{chat_id}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()["messages"][0]["content"]
        except (RequestException, KeyError, IndexError) as e:
            print(f"Error processing chat: {e}")
            return None
