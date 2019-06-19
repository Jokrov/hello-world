from selenium import webdriver
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
button = browser.find_element_by_css_selector("button.btn")
button.click()
#confirm = browser.switch_to.alert
#confirm.accept()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x=x_element.text
y=calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)


button = browser.find_element_by_css_selector("button.btn")
button.click()