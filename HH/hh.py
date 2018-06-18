from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
import traceback
import time

# настройки драйвера
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome('C:\\Users\MetalStyler\\PycharmProjects\\HHeroes\\chromedriver.exe',
                          desired_capabilities=capa)
driver.set_window_size(1280, 1024)
wait = WebDriverWait(driver, 10)

# переходим на сайт, пытаемся отловить и закрыть алерт
driver.get("http://hentaiheroes.com")
try:
    element = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("Алерт пойман и закрыт")
except TimeoutException:
    print("Алерта не было")

# логинимся
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hh_game"]')))
driver.switch_to.frame(driver.find_element_by_css_selector('#hh_game'))
driver.find_element_by_xpath('//*[@id="contains_all"]/header/div/a[1]').click()
driver.find_element_by_xpath('//*[@id="popup_login_form"]/form/div/input[1]').send_keys('metalstyler@gmail.com')
driver.find_element_by_xpath('//*[@id="popup_login_form"]/form/div/input[2]').send_keys('A217427h')
driver.find_element_by_css_selector('#popup_login_form > form > div > div:nth-child(14) > button').click()

# переходим к актуальному противнику через продолжение квеста
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="homepage"]/a[4]')))
driver.find_element_by_xpath('//*[@id="homepage"]/a[4]').click()
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#breadcrumbs > a:nth-child(5)')))
driver.find_element_by_css_selector('#breadcrumbs > a:nth-child(5)').click()

# сюда будут считаться успешно потраченные шансы
chances = 0

# проводим файты
for i in range(1, 20):
    try:
        # стартуем файт и скипаем бой
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="worldmap"]/a[8]')))
        driver.find_element_by_xpath('//*[@id="worldmap"]/a[8]').click()
        # time.sleep(1)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="battle_middle"]/button[1]')))
        driver.find_element_by_xpath('//button[@class="green_text_button"]').click()
        # time.sleep(1)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="battle_middle"]/button[2]')))
        driver.find_element_by_xpath('//*[@id="battle_middle"]/button[2]').click()
        time.sleep(1)
        try:
            element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//div[@id="battle_win"]/button[@class="blue_text_button"][text()= " Ok "]')))
            driver.find_element_by_xpath(
                '//div[@id="battle_win"]/button[@class="blue_text_button"][text()= " Ok "]').click()
            print("Потрачен 1 шанс, победа")
        except:
            element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//div[@id="battle_lose"]/button[@class="blue_text_button"][text()= " Ok "]')))
            driver.find_element_by_xpath(
                '//div[@id="battle_lose"]/button[@class="blue_text_button"][text()= " Ok "]').click()
            print("Потрачен 1 шанс, проигрыш")
        chances = chances + 1

    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())

    print("Потрачено " + chances + " шансов")
driver.close()
