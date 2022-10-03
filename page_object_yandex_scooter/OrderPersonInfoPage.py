from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPersonInfoPage:
    name = [By.XPATH, '//*[@placeholder="* Имя"]']
    last_name = [By.XPATH, '//*[@placeholder="* Фамилия"]']
    address = [By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]']
    phone = [By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]']
    subway_station = [By.XPATH, '//*[@placeholder="* Станция метро"]']
    chosen_station = [By.XPATH, '//li[@class="select-search__row"]']
    then_button = [By.XPATH, '//button[contains(text(),"Далее")]']
    name_error_message = [By.XPATH, '//div[contains(text(),"Введите корректное имя")]']

    def __init__(self, driver):
        self.driver = driver

    def fill_all_fields_about_person(self, name, last_name, address, phone):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.subway_station).click()
        self.driver.find_element(*self.chosen_station).click()
        self.driver.find_element(*self.phone).send_keys(phone)
        self.wait_for_then_button_enabled()
        self.driver.find_element(*self.then_button).click()

    def check_error_with_name(self):
        return self.driver.find_element(*self.name_error_message).is_displayed()

    def wait_for_then_button_enabled(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.then_button))
