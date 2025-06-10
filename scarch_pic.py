import selenium
import selenium.webdriver

browser = selenium.webdriver.Chrome()

browser.get("https://bilibili.com")
browser.close()