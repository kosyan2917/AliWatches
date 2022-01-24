import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
import vk_api
def write_msg(user_id):
    print(user_id)
    vk.method('messages.send', {'peer_id':int(user_id),'message': "Бот типа нажал на кнопку",'random_id':int(time.time()*1000)})

with open("data.txt", 'r') as f:
    login = f.readline()
    pw = f.readline()
    user_id = f.readline()
    token = f.readline()
print(user_id)
url = "https://login.aliexpress.ru/"
vk = vk_api.VkApi(token=token) #Авторизоваться как сообщество
driver = webdriver.Chrome('chromedriver.exe')
wait = WebDriverWait(driver, 30)
driver.get(url)
element = driver.find_element_by_xpath('.//*[text()="Вход по номеру телефона"]')
element.click()
element = driver.find_element_by_xpath('//*[@id="fm-login-id"]')
element.click()
element.send_keys(login)
element = driver.find_element_by_xpath('//*[@id="fm-login-password"]')
element.click()
element.send_keys(pw)
element = driver.find_element_by_xpath('//*[@id="__aer_root__"]/div/div[3]/div/div[1]/div[3]/div/button')
element.click()
time.sleep(5)
watch = "https://aliexpress.ru/item/1005003635068681.html?af=2136&utm_campaign=2136&aff_platform=api-new-link-generate&utm_medium=cpa&cn=10r68dzwleof3qcl7ybi8zwozxk82baj&dp=10r68dzwleof3qcl7ybi8zwozxk82baj&aff_fcid=8651bc9da8634af39d0df984c1e5f35d-1643055837014-07484-_9IusMY&cv=0&aff_fsk=_9IusMY&sk=_9IusMY&aff_trace_key=8651bc9da8634af39d0df984c1e5f35d-1643055837014-07484-_9IusMY&terminal_id=72c17bb1520446189165596024293de7&utm_source=aerkol&utm_content=0"
driver.get(watch)
while True:
    wait.until(EC.presence_of_element_located((By.XPATH, './/*[text()="Купить сейчас"]')))
    button = driver.find_element_by_xpath('.//*[text()="Купить сейчас"]')
    if button.is_enabled():
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        write_msg(user_id)
        wait.until(EC.presence_of_element_located((By.XPATH, './/input[@id="code"]')))
        input_field = driver.find_element_by_xpath('.//input[@id="code"]')
        input_field.click()
        input_field.send_keys("FORFUN2500")
        button = driver.find_element_by_xpath('.//button[@ae_button_type = "coupon_code"]')
        button.click()
    else:
        time.sleep(3)
        driver.get(watch)
    