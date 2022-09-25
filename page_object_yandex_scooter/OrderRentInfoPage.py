from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderRentInfoPage:
    date_field = [By.XPATH, '//*[@placeholder="* Когда привезти самокат"]']
    chosen_date = [By.XPATH, '//div[@aria-label="Choose пятница, 30-е сентября 2022 г."]']
    period_field = [By.XPATH, '//div[contains(text(),"* Срок аренды")]']
    chosen_period = [By.XPATH, '//div[contains(text(),"двое суток")]']
    scooter_color = [By.XPATH, '//label[contains(text(),"чёрный жемчуг")]']
    comment = [By.XPATH, '//*[@placeholder="Комментарий для курьера"]']
    make_order_button = [By.XPATH, '//button[contains(text(),"Назад")]/following-sibling::*']
    yes_button = [By.XPATH, '//button[contains(text(),"Да")]']
    successful_order_modal = [By.XPATH, '//div[contains(text(),"Заказ оформлен")]']

    def __init__(self, driver):
        self.driver = driver

    def fill_all_fields_about_rent(self, comment):
        self.driver.find_element(*self.date_field).click()
        self.driver.find_element(*self.chosen_date).click()
        self.driver.find_element(*self.period_field).click()
        self.driver.find_element(*self.chosen_period).click()
        self.driver.find_element(*self.scooter_color).click()
        self.driver.find_element(*self.comment).send_keys(comment)
        self.wait_for_finish_button_enabled()
        self.driver.find_element(*self.make_order_button).click()
        self.driver.find_element(*self.yes_button).click()

    def wait_for_finish_button_enabled(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.make_order_button))

    def successful_order_screen_is_displayed(self):
        return self.driver.find_element(*self.successful_order_modal).is_displayed()
