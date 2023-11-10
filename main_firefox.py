from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

print("Test Execution Started")

#driver_path = "D:\\Python\\Driver\\chromedriver.exe"
#service = Service(executable_path=driver_path)


# Создаем объект ChromeDriver, передавая сервис
#driver = webdriver.Chrome(service=service)


#driver = webdriver.Chrome()
driver=webdriver.Firefox()
# Открываем веб-страницу
#driver.get('http://192.168.201.151:8080/test')
driver.get('http://192.168.201.151:8080/B2ng/login')
driver.get_screenshot_as_file("1.png")

parent_div = driver.find_element(By.CLASS_NAME, "login")
input_elements = parent_div.find_elements(By.CSS_SELECTOR, "input[placeholder*='Користувач'][type='text']")
element = input_elements[0]
time.sleep(1)

wait = WebDriverWait(driver, 5)
element.clear()
element.send_keys("Ldap4JetB2Work")
driver.get_screenshot_as_file("2.png")
wait = WebDriverWait(driver, 5)
input_elements = parent_div.find_elements(By.CSS_SELECTOR, "input[placeholder*='Пароль'][type='password']")
element = input_elements[0]

element.clear()
element.send_keys('1qaz-2wsx-ASDF')
driver.get_screenshot_as_file("3.png")

wait = WebDriverWait(driver, 10)
input_elements = parent_div.find_elements(By.CSS_SELECTOR, "button[type='submit']")
element = input_elements[0]
element.click()
time.sleep(3)
driver.get_screenshot_as_file("4.png")

#wait = WebDriverWait(driver, 10)
#input_elements = parent_div.find_elements(By.CSS_SELECTOR, "class[type='b2ng-mfpb-caption']")
#input_elements = parent_div.find_elements(By.CSS_SELECTOR, ".b2ng-mfpb-caption")
#element = driver.find_element(By.XPATH, "/html/body/b2ng-root/b2ng-main-form/div[2]/b2ng-task-menu/cs-scrollable/div[1]/a/div[2]")
#element = driver.find_element_by_xpath("//div[@class='b2ng-mfpb-caption' and text()='Каса']")



element = input_elements[0]
element.click()
time.sleep(3)


driver.get_screenshot_as_file("4.png")


#button = driver.find_element(by=By.XPATH, value="//button[text()='Кнопка']")
# Кликнем по кнопке
#button.click()
#time.sleep(5)

# Закрываем браузер
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
