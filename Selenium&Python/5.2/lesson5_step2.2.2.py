from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Ivanov")
input3 = browser.find_element_by_css_selector("input:nth-child(6)")
input3.send_keys("EOF@Err.or")
input4 = browser.find_element_by_id("file")
current_dir=os.path.abspath(os.path.dirname(__file__))# получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')# добавляем к этому пути имя файла 
input4.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()