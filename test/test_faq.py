from selenium import webdriver
import page_object_yandex_scooter.HomePageYandexScooter as hps
import allure


class TestFAQHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка placeholder у поля email')
    def test_faq_question_price(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 2500)")
        home_page.open_question_price()

        assert home_page.get_answer_price()

    def test_faq_question_several_scooters(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 2500)")
        home_page.open_question_several_scooters()

        assert home_page.get_answer_several_scooters()

    def test_faq_question_rent_time(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 2800)")
        home_page.open_question_rent_time()

        assert home_page.get_answer_rent_time()

    def test_faq_question_scooter_today(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 3000)")
        home_page.open_question_scooter_today()

        assert home_page.get_answer_scooter_today()

    def test_faq_question_extend_or_return(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 3000)")
        home_page.open_question_extend_or_return()

        assert home_page.get_answer_extend_or_return()

    def test_faq_question_scooter_charge(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 3000)")
        home_page.open_question_scooter_charge()

        assert home_page.get_answer_scooter_charge()

    def test_faq_question_cancel_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 3000)")
        home_page.open_question_cancel_order()

        assert home_page.get_answer_cancel_order()

    def test_faq_question_outside_mkad(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = hps.HomePageScooter(self.driver)
        home_page.wait_for_load_home_page()
        self.driver.execute_script("window.scrollTo(0, 3000)")
        home_page.open_question_outside_mkad()

        assert home_page.get_answer_outside_mkad()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
