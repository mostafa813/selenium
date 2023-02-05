from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from faker import  Faker
fake = Faker()
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
actions = ActionChains(driver)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

#add new admin

# driver.get("https://setad.iranrahyaft.ir/signin")
# driver.maximize_window()
# sleep(2)
# user0 =  driver.find_element("id" , ":r0:")
# user0.send_keys("sajjad")
# passw0 = driver.find_element("id" , ":r1:")
# passw0.send_keys("asdf@1234")
# sleep(2)
# actions.send_keys(Keys.ENTER).perform()
# sleep(5)
# driver.find_element("xpath" , "//p[text()='خروج']").click()
# sleep(2)
# user0 =  driver.find_element("id" , ":r0:")
# user0.send_keys("sajjad")
# passw0 = driver.find_element("id" , ":r1:")
# passw0.send_keys("asdf@1234")
# driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
# sleep(5)
# driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root toggle-btn')]").click()
# sleep(1)
# driver.find_element("xpath" , "//p[text()='مدیریت ادمین ها']").click()
# sleep(1)
# driver.find_element("xpath", "(//div[@class='muirtl-dufqpb']//p)[3]").click()
# sleep(1)
# name0 = driver.find_element("xpath","//label[text()='نام']/following::input")
# name0.send_keys("mostafa_kashi")
# user = driver.find_element("xpath","//label[text()='نام کاربری']/following::input")
# user.send_keys("mostafa10")
# passw1 = driver.find_element("xpath" , "//label[text()='رمز عبور']/following::input")
# passw1.send_keys("kashi24M")
# email = driver.find_element("xpath","//label[text()='ایمیل']/following::input")
# email.send_keys("mostafakashi813@gmail.com")
# sleep(1)
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# sleep(2)
# el= driver.find_element("xpath","//div[@id='__next']/div[1]/div[2]/main[1]/form[1]/div[3]/button[2]/div[1]/p[1]")
# actions.click(el).perform()
# sleep(2)
# driver.find_element("xpath" , "//p[text()='مدیریت ادمین ها']").click()
# sleep(1)
#
# driver.find_element("xpath","//div[contains(@class,'MuiSelect-select MuiTablePagination-select')]").click()
# driver.find_element("xpath","//li[@data-value='-1']").click()
# sleep(3)
# dom = driver.page_source
# assert 'mostafa10' in dom

#add new setad 1

names = [fake.unique.user_name() for i in range(3)]
fake_name=names[0]
fake_username=names[1]
fake_name_manager=names[2]


driver.get("https://setad.iranrahyaft.ir/signin")
driver.maximize_window()
sleep(1)
user0 = driver.find_element("id" , ":r0:")
user0.send_keys("sajjad")
passw0 = driver.find_element("id" , ":r1:")
passw0.send_keys("asdf@1234")
sleep(1)
actions.send_keys(Keys.ENTER).perform()
sleep(1)
driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root toggle-btn')]").click()
sleep(1)
driver.find_element("xpath" , "//p[text()='لیست ستاد ها']").click()
sleep(1)
driver.find_element("xpath" , "//p[text()='افزودن']").click()
sleep(1)
name1 = driver.find_element("xpath" , "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]")
# fake_name=fake.unique.first_name()
name1.send_keys(fake_name)
user1 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]")
# fake_username=fake.unique.first_name()
user1.send_keys(fake_username)
name2 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
# fake_name_manager=fake.unique.first_name()
name2.send_keys(fake_name_manager)
user2 = driver.find_element("xpath" , "(//label[text()='نام کاربری'])[2]/following::input")
fake_username_manager=fake.first_name()
user2.send_keys(fake_username_manager)
passw = driver.find_element("name" , "password")
passw.send_keys("TEST")
sleep(1)
driver.find_element("xpath"  , "//div[@id='__next']/div[1]/div[2]/main[1]/form[1]/div[3]/button[2]/div[1]/p[1]").click()
sleep(5)

toast = driver.find_element("css selector", ".SnackbarContainer-bottom").text

assert toast == "با موفقیت انجام شد"
# for i in '123456789':
#     # import pdb; pdb.set_trace()
#     toast = driver.find_element("css selector", ".SnackbarContainer-bottom")
#     if toast:
#         break
#     else:
#         sleep(.5)
#         continue


sleep(1)
driver.find_element("xpath" , "//p[text()='لیست ستاد ها']").click()
sleep(1)
driver.find_element("xpath" , "//div[contains(@class,'MuiSelect-select MuiTablePagination-select')]").click()
sleep(1)
driver.find_element("xpath" , "//li[text()='همه']").click()
dom = driver.page_source
assert fake_name in dom
sleep(1)
driver.find_element("xpath","//p[text()='خروج']").click()
sleep(2)

driver.find_element("id" , ":r0:").send_keys(fake_username)
sleep(1)
driver.find_element("id" , ":r1:").send_keys("TEST")
sleep(4)
driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
sleep(5)


#add new setad 2


# driver.get("https://setad.iranrahyaft.ir/signin")
# driver.maximize_window()
# sleep(2)
# user0 =  driver.find_element("id" , ":r0:")
# user0.send_keys("sajjad")
# passw0 = driver.find_element("id" , ":r1:")
# passw0.send_keys("asdf@1234")
# sleep(2)
# actions.send_keys(Keys.ENTER).perform()
# sleep(5)
# driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root toggle-btn')]").click()
# sleep(1)
# driver.find_element("xpath" , "//p[text()='لیست ستاد ها']").click()
# sleep(1)
# driver.find_element("xpath" , "//p[text()='افزودن']").click()
# sleep(1)
# name1 = driver.find_element("xpath" , "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]")
# name1.send_keys("ستاد تست")
# user1 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]")
# user1.send_keys("test_me9")
# name2 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
# name2.send_keys("ستاد تست")
# user2 = driver.find_element("xpath" , "(//label[text()='نام کاربری'])[2]/following::input")
# user2.send_keys("test_me2")
# passw = driver.find_element("name" , "password")
# passw.send_keys("TEST")
# sleep(3)
# actions.send_keys(Keys.ENTER).perform()
# sleep(6)



# driver.get("https://setad.iranrahyaft.ir/signin")
# driver.maximize_window()
# sleep(3)
# user0 =  driver.find_element("id" , ":r0:")
# user0.send_keys("sajjad")
# passw0 = driver.find_element("id" , ":r1:")
# passw0.send_keys("asdf@1234")
# sleep(3)
# actions.send_keys(Keys.ENTER).perform()
# sleep(3)
# driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root toggle-btn')]").click()
# sleep(3)
# driver.find_element("xpath" , "//p[text()='آمار ستاد ها']").click()
# sleep(3)
# driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root toggle-btn')]").click()
# sleep(5)
# el2 = driver.find_element("xpath" , "//p[text()='نمایش لیستی']").click()
# sleep(5)
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# sleep(3)
# driver.find_element("xpat" , "//table[contains(@class,'MuiTable-root muirtl-mhd3ns')]/tbody[1]/tr[1]/td[7]/button[1]/div[1]/p[1]").click()
# sleep(4)






