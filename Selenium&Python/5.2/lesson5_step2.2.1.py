from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")

x_element = browser.find_element_by_id("input_value")
print(x_element)
x=x_element.text
y=calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
box = browser.find_element_by_id("robotCheckbox")
box.click()


bocx = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", bocx) #Проскроллить страницу вниз.
bocx.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()