from selenium import webdriver
def calc(x,y):
  return str(int(x)+int(y))
browser = webdriver.Chrome()
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1")

x_element = browser.find_element_by_id("num1")
x=x_element.text
y_element = browser.find_element_by_id("num2")
y=y_element.text
q=calc(x,y)
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(q) 





button = browser.find_element_by_css_selector("button.btn")
button.click()