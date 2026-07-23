import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_text_presence(browser):
    wait = WebDriverWait(browser, 10)
    frame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))
    target_text = "semper posuere integer et senectus justo curabitur."
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    text_element = next(paragraph for paragraph in paragraphs if target_text in paragraph.text)

    assert text_element.is_displayed()
