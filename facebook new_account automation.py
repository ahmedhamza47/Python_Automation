from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
print("sample test case started")
driver = webdriver.Chrome(executable_path="C:/drivers/chromedriver_win32/chromedriver.exe")

driver.maximize_window()
driver.get('https://www.facebook.com/')

driver.find_element_by_id('u_0_2').send_keys(Keys.ENTER)
time.sleep(3)
# new_driver = driver.switch_to_alert()

driver.find_element_by_name('firstname').send_keys('Alex')
time.sleep(2)
driver.find_element_by_name('lastname').send_keys('Hood')
time.sleep(2)
driver.find_element_by_name('reg_email__').send_keys('9861329826')
time.sleep(2)
driver.find_element_by_name('reg_passwd__').send_keys('@lexw00d_1')
time.sleep(2)

month = Select(driver.find_element_by_name('birthday_month'))
month.select_by_index(2)
time.sleep(2)

day = Select(driver.find_element_by_name('birthday_day'))
day.select_by_index(3)
time.sleep(2)

year = Select(driver.find_element_by_name('birthday_year'))
year.select_by_visible_text('2000')
time.sleep(2)
driver.find_element_by_id('u_1_3').is_selected()
driver.find_element_by_id('u_1_3').click()
time.sleep(2)

driver.find_element_by_name('websubmit').send_keys(Keys.ENTER)

time.sleep(10)
print('sample test successfully completed')


driver.close()