import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()


def test_button_text_changed(driver):
    wait = WebDriverWait(driver, 10)

    text_field = wait.until(EC.visibility_of_element_located((By.ID, "newButtonName")))
    button = wait.until(EC.visibility_of_element_located((By.ID, "updatingButton")))

    text_field.send_keys("ITCH")
    button.click()

    assert button.text == "ITCH"
