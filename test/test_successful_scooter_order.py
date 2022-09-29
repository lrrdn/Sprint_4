import allure
import page_object_yandex_scooter.HomePageYandexScooter as hps
import page_object_yandex_scooter.OrderPersonInfoPage as oip
import page_object_yandex_scooter.OrderRentInfoPage as orp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSuccessfulScooterOrder:

    @allure.title('Проверка создания заказа через кнопку вверху страницы')
    def test_make_order_via_up_button(self, driver):

        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        home_page.wait_for_load_home_page()
        home_page.click_order_up_button()
        order_info_page = oip.OrderPersonInfoPage(driver)
        order_info_page.fill_all_fields_about_person("Лера", "Родина", "Москва Кутузовский пр 24", "892199999999")
        order_rent_info_page = orp.OrderRentInfoPage(driver)
        order_rent_info_page.fill_all_fields_about_rent("Позвонить перед приездом")

        assert order_rent_info_page.successful_order_screen_is_displayed()

    @allure.title('Проверка создания заказа через кнопку внизу страницы')
    def test_make_order_via_down_button(self, driver):

        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        home_page.wait_for_load_home_page()
        driver.execute_script("window.scrollTo(0, 2000)")
        home_page.click_order_down_button()
        order_info_page = oip.OrderPersonInfoPage(driver)
        order_info_page.fill_all_fields_about_person("Егор", "Лебедев", "Москва Чистые пруды 35", "89990000000")
        order_rent_info_page = orp.OrderRentInfoPage(driver)
        order_rent_info_page.fill_all_fields_about_rent("Домофона нет")

        assert order_rent_info_page.successful_order_screen_is_displayed()

    @allure.title('Проверка создания заказа с пустым комментарием')
    def test_make_order_via_up_button_empty_comment(self, driver):

        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        home_page.wait_for_load_home_page()
        home_page.click_order_up_button()
        order_info_page = oip.OrderPersonInfoPage(driver)
        order_info_page.fill_all_fields_about_person("Тест", "Тестов", "Балашиха", "89991234567")
        order_rent_info_page = orp.OrderRentInfoPage(driver)
        order_rent_info_page.fill_all_fields_about_rent("")

        assert order_rent_info_page.successful_order_screen_is_displayed()

    @allure.title('Проверка создания заказа с некорректным именем латиницей')
    def test_make_order_via_down_button_incorrect_name(self, driver):

        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        home_page.wait_for_load_home_page()
        driver.execute_script("window.scrollTo(0, 2000)")
        home_page.click_order_down_button()
        order_info_page = oip.OrderPersonInfoPage(driver)
        order_info_page.fill_all_fields_about_person("RRR", "Иванов", "Неизвестный город", "80000000000")

        assert order_info_page.check_error_with_name()

    @allure.title('Проверка перехода по клику на кнопку с лого Самоката')
    def test_check_click_scooter_logo(self, driver):

        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        home_page.click_scooter_logo()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода по клику на кнопку с лого Яндекс')
    def test_check_click_yandex_logo(self, driver):

        wait = WebDriverWait(driver, 10)
        home_page = hps.HomePageScooter(driver)
        home_page.open_page(driver)
        original_window = driver.current_window_handle
        home_page.click_yandex_logo()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        wait.until(EC.title_is("Дзен"))

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
