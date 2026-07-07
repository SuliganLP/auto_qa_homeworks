import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 768)  # у меня в этом разрешении заработало, в родном - выбрасывает ошибку,
    # так как элемент вне зоны видимости
    yield driver
    driver.quit()


def test_itcareerhub_callback_popup(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(5)

    logo = driver.find_element(By.CSS_SELECTOR, "img")
    assert logo.is_displayed()

    programs = driver.find_element(By.LINK_TEXT, "Программы")
    assert programs.is_displayed()

    payment = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert payment.is_displayed()

    about = driver.find_element(By.LINK_TEXT, "О нас")
    assert about.is_displayed()

    reviews = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert reviews.is_displayed()

    blog = driver.find_element(By.LINK_TEXT, "Блог")
    assert blog.is_displayed()

    ru_button = driver.find_element(By.LINK_TEXT, "ru")
    assert ru_button.is_displayed()

    de_button = driver.find_element(By.LINK_TEXT, "de")
    assert de_button.is_displayed()

    sleep(3)

    about.click()

    contacts = driver.find_element(By.LINK_TEXT, "Контакты")
    assert contacts.is_displayed()
    contacts.click()

    sleep(3)

    callbacks = driver.find_elements(By.CSS_SELECTOR, "a[href*='popup:form-tr']")

    callback_was_clicked = False

    for callback in callbacks:
        if callback.is_displayed() and callback.text.strip() == "ОБРАТНЫЙ ЗВОНОК":
            callback.click()
            callback_was_clicked = True
            break

    assert callback_was_clicked, "Кнопка 'ОБРАТНЫЙ ЗВОНОК' не найдена или не отображается"

    sleep(2)

    popup = driver.find_element(By.CSS_SELECTOR, ".t-popup_show")

    assert popup.is_displayed()
    assert "Запишитесь на бесплатную карьерную консультацию" in popup.text
