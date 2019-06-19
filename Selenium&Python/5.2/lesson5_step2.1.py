from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x_element = browser.find_element_by_css_selector("img")
x_element=x_element.get_attribute("valuex")
print(x_element)
x=x_element
print(x)
y=calc(x)
print(x)


input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
box = browser.find_element_by_id("robotCheckbox")
box.click()
bocx = browser.find_element_by_id("robotsRule")
bocx.click()



button = browser.find_element_by_css_selector("button.btn")
button.click()