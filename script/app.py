from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://localhost")

def print_text(browser):
	h1 = browser.find_element_by_tag_name("h1")
	text = browser.find_element_by_id("text")
	print(h1.text + ": " + text.text)

def click_dropdown(browser):
	dropdown = browser.find_element_by_class_name("dropdown-toggle")
	dropdown.click()

def click_link(browser):
	bClickNextButton = False
	buttonList = browser.find_elements_by_class_name("dropdown-item")
	for button in buttonList:
		if 'active' in button.get_attribute("class").split():
			bClickNextButton = True
		elif bClickNextButton:
			button.click()
			print_text(browser)
			break


# 1st page text
print_text(browser)

buttonCount = len(browser.find_elements_by_class_name("dropdown-item"))

# click link for each remaining item
for _ in range(1, buttonCount):
	click_dropdown(browser)
	click_link(browser)

browser.close()
