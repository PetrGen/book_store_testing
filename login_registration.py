#Registration_login: регистрация аккаунта

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(2)
# driver.find_element_by_css_selector("#menu-item-50>a").click()
# driver.find_element_by_id("reg_email").send_keys("grigorov@mail.ru")
# driver.find_element_by_id("reg_password").send_keys("petr777!!!...")
# time.sleep(2)
# driver.find_element_by_css_selector("#customer_login > div.u-column2.col-2 > form").click()
# driver.find_element_by_css_selector("input[name='register']").click()
# driver.quit()


#Registration_login: логин в систему

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_css_selector("#menu-item-50>a").click()
# driver.find_element_by_css_selector('input[id="username"]').send_keys("grigorov@mail.ru")
# driver.find_element_by_css_selector('input[id="password"]').send_keys("petr777!!!...")
# driver.find_element_by_css_selector('input[name="login"]').click()
# log=driver.find_element_by_link_text("Logout")
# logtxt=log.text
# assert logtxt=="Logout"
# driver.quit()



