from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def wrong_city():
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

        city_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/aside[4]/div[2]/div/div/div/div/div/div[2]/div/input')))
        city_input.send_keys("абвабв")

        final_city = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div/div/div/aside[4]/div[2]/div/div/div/div/div/div[3]/div[2]/div/div')))

        assert final_city.text == "к сожалению, ничего не найдено", "Выбранный город не отображается корректно"

        print("Тест wrong_city успешно выполнен")

    except Exception as e:
        print(f"Тест wrong_city завершился с ошибкой: {e}")
    finally:
        driver.quit()
