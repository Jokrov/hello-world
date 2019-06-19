from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1")


input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
input3.send_keys("Smosk@mail.com")
input4 = browser.find_element_by_css_selector(".second_block input.first")
input4.send_keys("7777777")
input5 = browser.find_element_by_css_selector(".second_block input.second")
input5.send_keys("MemoryEr+ror")
button = browser.find_element_by_css_selector("button.btn")
button.click()