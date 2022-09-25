from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePageScooter:
    faq_question_1 = [By.XPATH, '//*[@class="accordion__item"][1]']
    answer_for_question_1 = [By.XPATH, '//p[contains(text(),"Сутки — 400 рублей. Оплата курьеру — наличными или '
                                       'картой.")]']
    faq_question_2 = [By.XPATH, '//*[@class="accordion__item"][2]']
    answer_for_question_2 = [By.XPATH, '//p[contains(text(),"Пока что у нас так: один заказ — один самокат. Если '
                                       'хотите покататься с друзьями, можете просто сделать несколько заказов — один '
                                       'за другим.")]']
    faq_question_3 = [By.XPATH, '//*[@class="accordion__item"][3]']
    answer_for_question_3 = [By.XPATH, '//p[contains(text(),"Допустим, вы оформляете заказ на 8 мая. Мы привозим '
                                       'самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, '
                                       'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
                                       'суточная аренда закончится 9 мая в 20:30.")]']
    faq_question_4 = [By.XPATH, '//*[@class="accordion__item"][4]']
    answer_for_question_4 = [By.XPATH, '//p[contains(text(),"Только начиная с завтрашнего дня. Но скоро станем '
                                       'расторопнее.")]']
    faq_question_5 = [By.XPATH, '//*[@class="accordion__item"][5]']
    answer_for_question_5 = [By.XPATH, '//p[contains(text(),"Пока что нет! Но если что-то срочное — всегда можно '
                                       'позвонить в поддержку по красивому номеру 1010.")]']
    faq_question_6 = [By.XPATH, '//*[@class="accordion__item"][6]']
    answer_for_question_6 = [By.XPATH, '//p[contains(text(),"Самокат приезжает к вам с полной зарядкой. Этого хватает '
                                       'на восемь суток — даже если будете кататься без передышек и во сне. Зарядка '
                                       'не понадобится.")]']
    faq_question_7 = [By.XPATH, '//*[@class="accordion__item"][7]']
    answer_for_question_7 = [By.XPATH, '//p[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, '
                                       'объяснительной записки тоже не попросим. Все же свои.")]']
    faq_question_8 = [By.XPATH, '//*[@class="accordion__item"][8]']
    answer_for_question_8 = [By.XPATH, '//p[contains(text(),"Да, обязательно. Всем самокатов! И Москве, и Московской '
                                       'области.")]']
    order_button_up = [By.CLASS_NAME, 'Button_Button__ra12g']

    order_button_down = [By.XPATH, '//*[@class="Home_FinishButton__1_cWm"]/child::*']

    scooter_logo = [By.XPATH, '//img[contains(@alt,"Scooter")]']
    yandex_logo = [By.XPATH, '//img[contains(@alt,"Yandex")]']

    def __init__(self, driver):
        self.driver = driver

    def open_question_price(self):
        self.driver.find_element(*self.faq_question_1).click()

    def get_answer_price(self):
        return self.driver.find_element(*self.answer_for_question_1).is_displayed()

    def open_question_several_scooters(self):
        self.driver.find_element(*self.faq_question_2).click()

    def get_answer_several_scooters(self):
        return self.driver.find_element(*self.answer_for_question_2).is_displayed()

    def open_question_rent_time(self):
        self.driver.find_element(*self.faq_question_3).click()

    def get_answer_rent_time(self):
        return self.driver.find_element(*self.answer_for_question_3).is_displayed()

    def open_question_scooter_today(self):
        self.driver.find_element(*self.faq_question_4).click()

    def get_answer_scooter_today(self):
        return self.driver.find_element(*self.answer_for_question_4).is_displayed()

    def open_question_extend_or_return(self):
        self.driver.find_element(*self.faq_question_5).click()

    def get_answer_extend_or_return(self):
        return self.driver.find_element(*self.answer_for_question_5).is_displayed()

    def open_question_scooter_charge(self):
        self.driver.find_element(*self.faq_question_6).click()

    def get_answer_scooter_charge(self):
        return self.driver.find_element(*self.answer_for_question_6).is_displayed()

    def open_question_cancel_order(self):
        self.driver.find_element(*self.faq_question_7).click()

    def get_answer_cancel_order(self):
        return self.driver.find_element(*self.answer_for_question_7).is_displayed()

    def open_question_outside_mkad(self):
        self.driver.find_element(*self.faq_question_8).click()

    def get_answer_outside_mkad(self):
        return self.driver.find_element(*self.answer_for_question_8).is_displayed()

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(self.faq_question_8))

    def click_order_up_button(self):
        self.driver.find_element(*self.order_button_up).click()

    def click_order_down_button(self):
        self.driver.find_element(*self.order_button_down).click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()
