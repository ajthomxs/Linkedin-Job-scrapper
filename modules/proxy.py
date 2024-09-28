from random import random
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_free_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies = []
    for row in soup.find(class_='table table-striped table-bordered').tbody.find_all('tr'):
        cols = row.find_all('td')
        ip = cols[0].text
        port = cols[1].text
        https = cols[6].text
        if https == 'yes':
            proxies.append(f"https://{ip}:{port}")
        else:
            proxies.append(f"http://{ip}:{port}")
    return proxies

def validate_proxy(proxy, test_url='https://httpbin.org/ip', timeout=5):
    try:
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=timeout)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def get_valid_proxies(proxies, max_proxies=20):
    valid = []
    for proxy in proxies:
        if validate_proxy(proxy):
            valid.append(proxy)
            if len(valid) >= max_proxies:
                break
    return valid

def get_random_proxy(proxies):
    return random.choice(proxies)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)"
    " Version/14.0 Safari/605.1.15",
    # Add more user agents
]

def get_random_user_agent():
    return random.choice(user_agents)

def create_driver(proxy, user_agent):
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")  # Optional: run in headless mode
    caps = webdriver.DesiredCapabilities.EDGE.copy()
    caps['excludeSwitches'] = ['enable-automation']
    caps['useAutomationExtension'] = False
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options,
        desired_capabilities=caps
    )
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

if __name__ == '__main__' :
    get_free_proxies()