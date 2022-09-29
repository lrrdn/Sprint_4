from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePageScooter:
    faq_question_1 = '//*[@class="accordion__item"][1]'
    answer_for_question_1 = '//p[contains(text(),"Сутки — 400 рублей. Оплата курьеру — наличными или картой.")]'
    faq_question_2 = '//*[@class="accordion__item"][2]'
    answer_for_question_2 = '//p[contains(text(),"Пока что у нас так: один заказ — один самокат. Если хотите ' \
                            'покататься с друзьями, можете просто сделать несколько заказов — один за другим.")] '
    faq_question_3 = '//*[@class="accordion__item"][3]'
    answer_for_question_3 = '//p[contains(text(),"Допустим, вы оформляете заказ на 8 мая. Мы привозим ' \
                            'самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, ' \
                            'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, ' \
                            'суточная аренда закончится 9 мая в 20:30.")]'
    faq_question_4 = '//*[@class="accordion__item"][4]'
    answer_for_question_4 = '//p[contains(text(),"Только начиная с завтрашнего дня. Но скоро станем ' \
                            'расторопнее.")]'
    faq_question_5 = '//*[@class="accordion__item"][5]'
    answer_for_question_5 = '//p[contains(text(),"Пока что нет! Но если что-то срочное — всегда можно ' \
                            'позвонить в поддержку по красивому номеру 1010.")]'
    faq_question_6 = '//*[@class="accordion__item"][6]'
    answer_for_question_6 = '//p[contains(text(),"Самокат приезжает к вам с полной зарядкой. Этого хватает ' \
                            'на восемь суток — даже если будете кататься без передышек и во сне. Зарядка ' \
                            'не понадобится.")]'
    faq_question_7 = '//*[@class="accordion__item"][7]'
    answer_for_question_7 = '//p[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, ' \
                            'объяснительной записки тоже не попросим. Все же свои.")]'
    faq_question_8 = '//*[@class="accordion__item"][8]'
    answer_for_question_8 = '//p[contains(text(),"Да, обязательно. Всем самокатов! И Москве, и Московской ' \
                            'области.")]'
    last_element_scroll = [By.XPATH, '//*[@class="accordion__item"][8]']
    order_button_up = [By.CLASS_NAME, 'Button_Button__ra12g']

    order_button_down = [By.XPATH, '//*[@class="Home_FinishButton__1_cWm"]/child::*']

    scooter_logo = [By.XPATH, '//img[contains(@alt,"Scooter")]']
    yandex_logo = [By.XPATH, '//img[contains(@alt,"Yandex")]']

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")

    def open_question(self, selector):
        self.driver.find_element(By.XPATH, selector).click()

    def get_answer(self, selector):
        WebDriverWait(self.driver, 5)
        return self.driver.find_element(By.XPATH, selector).is_displayed()

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(self.last_element_scroll))

    def click_order_up_button(self):
        self.driver.find_element(*self.order_button_up).click()

    def click_order_down_button(self):
        self.driver.find_element(*self.order_button_down).click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()
