import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def change_country():
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

        city_option = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[6]/div[2]/div/div/div/div/div/div/div[3]/div[1]/div/button')))
        city_option.click()

        list_country = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/aside[4]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div')))
        list_country.click()

        final_county = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[4]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/ul/li[2]/div')))
        final_county.click()

        ok_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div/aside[4]/div[2]/div/div/div/div/div[2]/div/footer/button[1]')))
        ok_button.click()

        time.sleep(7)

        final_city = wait.until(EC.presence_of_element_located(
            (By.XPATH,'/html/body/div/div/div/header/div[2]/div[1]/div/aside/div/div[1]/div[2]/div/span')))

        assert final_city.text == "Минск", "Выбранный город не отображается корректно"

        print("Тест change_country успешно выполнен")

    except Exception as e:
        print(f"Тест change_country завершился с ошибкой: {e}")
    finally:
        driver.quit()
