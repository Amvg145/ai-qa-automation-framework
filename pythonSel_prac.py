from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

search_box = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
)

search_box.send_keys("mobiles")
search_box.send_keys(Keys.ENTER)

first_item = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    )
)

name = first_item.find_element(By.CSS_SELECTOR, "h2 span").text
price = first_item.find_element(By.CSS_SELECTOR, ".a-price-whole").text

print(f"Name: {name}")
print(f"Price: ₹{price}")

driver.quit()