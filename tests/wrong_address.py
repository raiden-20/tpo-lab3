import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def wrong_address():
    options = Options()

    options.set_preference("geo.enabled", False)
    options.set_preference("geo.provider.network.url", "")
    options.set_preference("geo.prompt.testing", False)
    options.set_preference("geo.prompt.testing.allow", False)

    driver = webdriver.Firefox(options=options)

    try:
        driver.get("https://goldapple.ru/")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        select_address_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/header/div[2]/div[1]/div/aside/div/div[2]/button[1]')))
        select_address_button.click()

        address_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[1]/div/label/input')))
        address_input.send_keys("абвабв")
        address_input.send_keys(Keys.ENTER)

        final_address = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div')))
        assert final_address.text == "ничего не найдено", "Сообщение не отображается корректно"


        print("Тест wrong_address успешно выполнен")

    except Exception as e:
        print(f"Тест choose_address завершился с ошибкой: {e}")
    finally:
        driver.quit()
