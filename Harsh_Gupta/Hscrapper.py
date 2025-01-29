from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def google_search(query, max_results=10):
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
      
        driver.get("https://www.google.com")
        time.sleep(2)
        
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # Extract search results
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        links = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf a")
        
        search_results = []
        for i in range(min(len(results), max_results)):
            title = results[i].text
            link = links[i].get_attribute("href")
            search_results.append((title, link))
        
        return search_results
    
    finally:
        driver.quit()

if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = google_search(query)
    
    print("\nTop Search Results:")
    for idx, (title, link) in enumerate(results, 1):
        print(f"{idx}. {title} - {link}")
