# https://codeleading.com/article/49364349747/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# 模拟登陆qq邮箱
driver = webdriver.Firefox(executable_path = 'D:\getckodriver\geckodriver')
driver.get("https://mail.qq.com/")
time.sleep(5)
# 切换iframe
driver.switch_to.frame("login_frame")
# 用户名 密码
elem_user = driver.find_element_by_name("u")
elem_user.send_keys("1925432244")
elem_pwd = driver.find_element_by_name("p")
elem_pwd.send_keys("XXXXXX")
elem_but = driver.find_element_by_id("login_button")
# elem_pwd.send_keys(Keys.RETURN)
elem_but.click()
time.sleep(5)
# driver.quit()
