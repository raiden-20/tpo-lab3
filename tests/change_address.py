import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def change_address():
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
        address_input.send_keys("Арбат 10")

        address_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/ul/li[1]/div')))
        address_button.click()

        ok_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[3]/button')))
        ok_button.click()

        time.sleep(2)

        select_address_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/main/button/div[2]/div')))
        select_address_button.click()

        city_option = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[1]/div/button')))
        city_option.click()

        delivery_city = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[4]/div[2]/div/div/div/div/div/div[3]/div[2]/ul/li[2]/div')))
        delivery_city.click()

        address_input = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[1]/div/label/input')))
        address_input.send_keys("Троицкий 15")

        address_button = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/ul/li/div')))
        address_button.click()

        ok_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[3]/button')))
        ok_button.click()

        final_street = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/button/div[2]/div/span[1]')))
        final_house = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/button/div[2]/div/span[2]')))
        assert final_street.text == "Троицкий, ", "Выбранный адрес не отображается корректно"
        assert final_house.text == "15", "Выбранный адрес не отображается корректно"

        print("Тест change_address успешно выполнен")

    except Exception as e:
        print(f"Тест change_address завершился с ошибкой: {e}")
    finally:
        driver.quit()
