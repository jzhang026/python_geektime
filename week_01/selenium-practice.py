from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.witch_to_frame(browser.find_elements_by_tag_name('[ifram][0]'))
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]')
    btm1 = click()

    browser.find_element_by_xpath('//*[@id="username]').send_keys('2222@example.com')
    browser.find_element_by_id('password').send_keys('123123123')

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()