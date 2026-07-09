import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()


def test_images_load(driver):
    wait = WebDriverWait(driver, 10)

    third_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='award']")))
    third_image_alt = third_image.get_attribute("alt")

    assert third_image_alt == "award"
