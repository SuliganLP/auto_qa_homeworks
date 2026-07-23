import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    driver.maximize_window()

    try:
        cookie_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.fc-cta-consent")
            )
        )
        cookie_button.click()

    except TimeoutException:
        pass

    yield driver
    driver.quit()


def test_drag_and_drop(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='photo-manager']")))
    photos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery > li")))

    first_photo = photos[0]

    assert len(photos) == 4

    thrash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    ActionChains(browser).drag_and_drop(first_photo, thrash).perform()

    wait.until(lambda d: len(browser.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)

    photos_in_trash = browser.find_elements(By.CSS_SELECTOR, "#trash li")
    photos_in_gallery = browser.find_elements(By.CSS_SELECTOR, "#gallery > li")

    assert len(photos_in_trash) == 1
    assert len(photos_in_gallery) == 3
