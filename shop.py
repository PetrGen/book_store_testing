#Shop: отображение страницы товара

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
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.find_element_by_css_selector("li>a>img[title='Mastering HTML5 Forms']").click()
# name=driver.find_element_by_css_selector(".summary.entry-summary>h1")
# tname=name.text
# assert tname=="HTML5 Forms"
# time.sleep(5)
# driver.quit()


#Shop: количество товаров в категории

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
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.find_element_by_css_selector(".cat-item.cat-item-19>a").click()
# spis=driver.find_element_by_css_selector(".products.masonry-done")
# tspis=spis.text
# amount=tspis.count("ADD TO BASKET")
# amount1=str(amount)
# print("На странице отображается "+amount1+" элемент(а)")
# time.sleep(5)
# driver.quit()


#Shop: сортировка товаров

# import time
# from selenium.webdriver.support.select import Select
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
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# elem=driver.find_element_by_css_selector("form.woocommerce-ordering>select")
# element=elem.get_attribute("value")
# if element=="menu_order":
#     print("В селекторе выбран вариант сортировки по умолчанию")
# else: print("Ошибка выбора варианта сортировки")
# elem1=driver.find_element_by_css_selector("form.woocommerce-ordering>select")
# select=Select(elem1)
# select.select_by_value("price-desc")
# elem2=driver.find_element_by_css_selector("form.woocommerce-ordering>select")
# element2=elem2.get_attribute("value")
# if element2=="price-desc":
#     print("В селекторе выбрана сортировка от большей цены к меньшей")
# else: print("Ошибка выбора варианта сортировки")
# time.sleep(2)
# driver.quit()


#Shop: отображение, скидка товара

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_css_selector("#menu-item-50>a").click()
# driver.find_element_by_css_selector('input[id="username"]').send_keys("grigorov@mail.ru")
# driver.find_element_by_css_selector('input[id="password"]').send_keys("petr777!!!...")
# driver.find_element_by_css_selector('input[name="login"]').click()
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[1]/img').click()
# lastprice=driver.find_element_by_css_selector("del>.woocommerce-Price-amount.amount")
# tlastprice=lastprice.text
# assert tlastprice=="₹600.00"
# newprice=driver.find_element_by_css_selector("ins>span")
# tnewprice=newprice.text
# assert tnewprice=="₹450.00"
# driver.find_element_by_css_selector('div.images>a>img').click()
# WebDriverWait(driver,2).until(
# EC. visibility_of_element_located((By.ID, "fullResImage")))
# time.sleep(2)
# driver.find_element_by_css_selector(".pp_close").click()
# WebDriverWait(driver,2).until(
# EC. invisibility_of_element_located((By.ID, "fullResImage")))
# driver.quit()


#Shop: проверка цены в корзине

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_css_selector("#menu-item-50>a").click()
# driver.find_element_by_css_selector('input[id="username"]').send_keys("grigorov@mail.ru")
# driver.find_element_by_css_selector('input[id="password"]').send_keys("petr777!!!...")
# driver.find_element_by_css_selector('input[name="login"]').click()
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(4)
# item=driver.find_element_by_css_selector(".wpmenucart-contents>span.cartcontents")
# t_item=item.text
# print(t_item)
# assert t_item=="1 Item"
# price=driver.find_element_by_css_selector(".wpmenucart-contents>span.amount")
# t_price=price.text
# print(t_price)
# assert t_price=="₹180.00"
# time.sleep(2)
# driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
# subtotal= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td[data-title='Subtotal']>.woocommerce-Price-amount.amount"), "₹180.00"))
# total= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong>.woocommerce-Price-amount.amount"), "₹183.60"))
# time.sleep(3)
# driver.quit()


#Shop: работа в корзине

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
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.execute_script("window.scrollBy(0,300);")
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='content']/ul/li[5]/a[2]").click()
# time.sleep(1)
# driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
# time.sleep(1)
# driver.find_element_by_css_selector("td.product-remove>a[data-product_id='182']").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".woocommerce-message>a").click()
# c_lear=driver.find_element_by_css_selector(".cart_item:first-child>.product-quantity>div.quantity>input")
# c_lear.clear()
# time.sleep(2)
# c_lear.send_keys("3")
# driver.find_element_by_css_selector("input[name='update_cart']").click()
# va_lue=driver.find_element_by_css_selector(".cart_item:first-child>.product-quantity>div.quantity>input")
# valu_e=va_lue.get_attribute("value")
# assert valu_e=="3"
# time.sleep(2)
# driver.find_element_by_css_selector("[name='apply_coupon']").click()
# cupon=driver.find_element_by_css_selector(".woocommerce-error>li")
# t_cupon=cupon.text
# assert t_cupon=="Please enter a coupon code."
# driver.quit()


#Shop: покупка товара

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# time.sleep(1)
# driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.execute_script("window.scrollBy(0,300);")
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(2)
# driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".wc-proceed-to-checkout>a").click()
# link_check = WebDriverWait(driver, 10).until(
# EC.url_to_be("https://practice.automationtesting.in/checkout/"))
# driver.find_element_by_css_selector("#billing_first_name_field>input").clear()
# driver.find_element_by_css_selector("#billing_first_name_field>input").send_keys("Petr")
# WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#billing_first_name_field>input"), "Petr"))
# driver.find_element_by_css_selector("#billing_last_name_field>input").clear()
# driver.find_element_by_css_selector("#billing_last_name_field>input").send_keys("Grigorov")
# driver.find_element_by_css_selector("#billing_phone_field>input").clear()
# driver.find_element_by_css_selector("#billing_phone_field>input").send_keys("89523871759")
# driver.find_element_by_css_selector("#s2id_billing_country>a.select2-choice>.select2-arrow>b").click()
# driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
# driver.find_element_by_css_selector(".select2-match").click()
# driver.find_element_by_css_selector("#billing_address_1_field>input").clear()
# driver.find_element_by_css_selector("#billing_address_1_field>input").send_keys("Nevsky ave.77")
# driver.find_element_by_css_selector("#billing_city_field>input").clear()
# driver.find_element_by_css_selector("#billing_city_field>input").send_keys("Saint-Petersburg")
# driver.find_element_by_css_selector("#billing_state_field>input").clear()
# driver.find_element_by_css_selector("#billing_state_field>input").send_keys("SZFO")
# time.sleep(1)
# driver.find_element_by_css_selector("#billing_postcode_field>input").clear()
# driver.find_element_by_css_selector("#billing_postcode_field>input").send_keys("195271")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,600);")
# time.sleep(2)
# driver.find_element_by_id("payment_method_cheque").click()
# driver.find_element_by_css_selector("#place_order").click()
# WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
#                                  'Thank you. Your order has been received.'))
# WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "table.shop_table.order_details > tfoot > tr:nth-child(3) > td"),
#                                  'Check Payments'))
# driver.quit()



