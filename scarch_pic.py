import selenium
import selenium.webdriver

if __name__ == "__main__":
    browser = selenium.webdriver.Chrome()

    browser.get("https://bilibili.com")
    browser.close()
