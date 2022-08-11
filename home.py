#Home: добавление комментария

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
driver.execute_script("window.scrollBy(0,600);")
driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0>div>ul>li>.woocommerce-LoopProduct-link>h3").click()
driver.execute_script("window.scrollBy(0,200);")
driver.find_element_by_css_selector("li.reviews_tab>a").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,400);")
driver.find_element_by_css_selector("p.stars>span>a.star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Petr")
driver.find_element_by_id("email").send_keys("petr_grigorov@mail.ru")
time.sleep(2)
driver.find_element_by_css_selector(".form-submit>#submit").click()