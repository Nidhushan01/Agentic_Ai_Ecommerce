from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_product_data_amazon(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir=/tmp/profile-{time.time()}")

    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        price_element = soup.select_one("#priceblock_ourprice, #priceblock_dealprice, .a-price-whole")
        price = None
        if price_element:
            price_text = price_element.get_text().replace('$', '').replace(',', '').strip()
            fractional = price_element.find_next_sibling('.a-price-fraction')
            if fractional:
                price_text += '.' + fractional.get_text().strip()
            try:
                price = float(price_text)
            except:
                price = None

        rating_element = soup.select_one("span.a-icon-alt")
        rating = float(rating_element.text.split()[0]) if rating_element else None

        return {"price": price, "rating": rating}
    except Exception as e:
        print(f"Selenium error: {e}")
        return {"price": None, "rating": None}
    finally:
        if driver:
            driver.quit()
