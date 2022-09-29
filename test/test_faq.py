import page_object_yandex_scooter.HomePageYandexScooter as hps
import allure
import pytest


class TestFAQHomePage:

    @pytest.mark.parametrize('question_selector, answer_selector',
                             [(hps.HomePageScooter.faq_question_1, hps.HomePageScooter.answer_for_question_1),
                              (hps.HomePageScooter.faq_question_2, hps.HomePageScooter.answer_for_question_2),
                              (hps.HomePageScooter.faq_question_3, hps.HomePageScooter.answer_for_question_3),
                              (hps.HomePageScooter.faq_question_4, hps.HomePageScooter.answer_for_question_4),
                              (hps.HomePageScooter.faq_question_5, hps.HomePageScooter.answer_for_question_5),
                              (hps.HomePageScooter.faq_question_6, hps.HomePageScooter.answer_for_question_6),
                              (hps.HomePageScooter.faq_question_7, hps.HomePageScooter.answer_for_question_7),
                              (hps.HomePageScooter.faq_question_8, hps.HomePageScooter.answer_for_question_8)])
    @allure.title('Проверка FAQ - каждый вопрос и ответ соответствуют друг другу')
    def test_faq_question_price(self, driver, question_selector, answer_selector):
        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        home_page.wait_for_load_home_page()
        driver.execute_script("window.scrollTo(0, 2800)")
        home_page.wait_for_load_home_page()
        home_page.open_question(question_selector)
        home_page.wait_for_load_home_page()

        assert home_page.get_answer(answer_selector)
