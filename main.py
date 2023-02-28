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


names = [fake.user_name() for i in range(4)]
fake_name=names[0]
fake_username=names[1]
fake_name_manager=names[2]
fake_username_manager=names[3]



def add_new_admin():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(2)
    user0 =  driver.find_element("id" , ":r0:")
    user0.send_keys("sajjad")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("asdf@1234")
    sleep(2)
    actions.send_keys(Keys.ENTER).perform()
    sleep(5)
    driver.find_element("xpath" , "//p[text()=' مدیریت ادمین ها']").click()
    sleep(1)
    driver.find_element("xpath", "//p[text()='افزودن']").click()
    sleep(1)
    name0 = driver.find_element("xpath","//label[text()='نام']/following::input")
    fake_name = names[0]
    name0.send_keys(fake_name)
    user = driver.find_element("xpath","//label[text()='نام کاربری']/following::input")
    fake_username = names[1]
    user.send_keys(fake_username)
    passw1 = driver.find_element("xpath" , "//label[text()='رمز عبور']/following::input")
    passw1.send_keys("kashi24M")
    email = driver.find_element("xpath","//label[text()='ایمیل']/following::input")
    email.send_keys("mostafakashi813@gmail.com")
    driver.find_element("xpath","//p[text()='تایید اطلاعات تکمیل شده']").click()
    sleep(1)
    actions.move_by_offset(300,300).click().perform()
    sleep(1)
    driver.find_element("xpath","//div[contains(@class,'MuiSelect-select MuiTablePagination-select')]").click()
    sleep(1)
    driver.find_element("xpath","//li[text()='همه']").click()
    sleep(3)
    dom = driver.page_source
    assert 'mostafa10' in dom




def add_new_setad_1():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(1)
    user0 = driver.find_element("id" , ":r0:")
    user0.send_keys("sajjad")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("asdf@1234")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(1)
    driver.find_element("xpath" , "//p[text()='لیست ستاد ها']").click()
    sleep(1)
    driver.find_element("xpath" , "//p[text()='افزودن']").click()
    sleep(1)
    name1 = driver.find_element("xpath" , "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]")
    name1.send_keys(fake_name)
    user1 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]")
    user1.send_keys(fake_username)
    name2 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
    name2.send_keys(fake_name_manager)
    user2 = driver.find_element("xpath" , "(//label[text()='نام کاربری'])[2]/following::input")
    user2.send_keys(fake_username_manager)
    passw = driver.find_element("name" , "password")
    passw.send_keys("TEST")
    sleep(1)
    driver.find_element("xpath","//label[text()='تکرار رمز عبور']/following::input").send_keys("TEST")
    sleep(1)
    addres= driver.find_element("xpath","//label[text()='آدرس']/following::input")
    addres.send_keys("tehran")
    sleep(1)
    driver.find_element("xpath","//p[text()='انتخاب از نقشه']").click()
    sleep(4)
    driver.find_element("css selector","html>body>div:nth-of-type(2)>div:nth-of-type(3)>div>div>div:nth-of-type(3)>span>img").click()
    sleep(1)
    driver.find_element("xpath"  , "//p[text()='تایید اطلاعات تکمیل شده']").click()
    actions.move_by_offset(300,300).click().perform()
    sleep(5)
    toast=driver.find_element("id","notistack-snackbar").text
    assert toast == "با موفقیت انجام شد"
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

    driver.find_element("id" , ":r0:").send_keys(fake_username_manager)
    sleep(1)
    driver.find_element("id" , ":r1:").send_keys("TEST")
    sleep(4)
    driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(5)



# def add_new_setad():
#     driver.get("https://dev-dashboard.hnaya.app/signin")
#     driver.maximize_window()
#     sleep(2)
#     user0 =  driver.find_element("id" , ":r0:")
#     user0.send_keys("sajjad")
#     passw0 = driver.find_element("id" , ":r1:")
#     passw0.send_keys("asdf@1234")
#     sleep(2)
#     actions.send_keys(Keys.ENTER).perform()
#     sleep(5)
#     driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root toggle-btn')]").click()
#     sleep(5)
#     driver.find_element("xpath" , "//p[text()='لیست ستاد ها']").click()
#     sleep(1)
#     driver.find_element("xpath" , "//p[text()='افزودن']").click()
#     sleep(1)
#     name1 = driver.find_element("xpath" , "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]")
#     name1.send_keys(fake_name)
#     user1 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]")
#     user1.send_keys(fake_username)
#     name2 = driver.find_element("xpath" , "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]")
#     name2.send_keys(fake_name_manager)
#     user2 = driver.find_element("xpath" , "(//label[text()='نام کاربری'])[2]/following::input")
#     user2.send_keys(fake_username_manager)
#     passw = driver.find_element("name" , "password")
#     passw.send_keys("TEST")
#     sleep(3)
#     actions.send_keys(Keys.ENTER).perform()
#     sleep(3)
#     toast=driver.find_element("id","notistack-snackbar").text
#     assert toast == "با موفقیت انجام شد"
#     sleep(1)
#     driver.find_element("xpath" , "//p[text()='لیست ستاد ها']").click()
#     sleep(1)
#     driver.find_element("xpath" , "//div[contains(@class,'MuiSelect-select MuiTablePagination-select')]").click()
#     sleep(1)
#     driver.find_element("xpath" , "//li[text()='همه']").click()
#     dom = driver.page_source
#     assert fake_name in dom
#     sleep(1)
#     driver.find_element("xpath","//p[text()='خروج']").click()
#     sleep(2)
#     driver.find_element("id" , ":r0:").send_keys(fake_username_manager)
#     sleep(1)
#     driver.find_element("id" , ":r1:").send_keys("TEST")
#     sleep(4)
#     driver.find_element("xpath" , "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
#     sleep(5)






def test_reject_request():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(1)
    user0 =  driver.find_element("id" , ":r0:")
    user0.send_keys("sajjad")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("asdf@1234")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath","//div[@id='__next']/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[2]/div[1]").click()
    sleep(2)
    driver.find_element("xpath", "//p[text()='بله']").click()
    sleep(2)
    text=driver.find_element("id","notistack-snackbar").text
    assert text=="با موفقیت رد شد"





def test_accept_request():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(1)
    user0 =  driver.find_element("id" , ":r0:")
    user0.send_keys("sajjad")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("asdf@1234")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath","//p[text()='تائید']").click()
    sleep(2)
    driver.find_element("xpath", "//p[text()='بله']").click()
    sleep(2)
    text=driver.find_element("id","notistack-snackbar").text
    assert text=="با موفقیت تایید شد"




def test_not_accept_request():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(1)
    user0 =  driver.find_element("id" , ":r0:")
    user0.send_keys("sajjad")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("asdf@1234")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath","//p[text()='تائید']").click()
    sleep(2)
    driver.find_element("xpath", "//p[text()='خیر']").click()
    sleep(2)
    # text=driver.find_element("id","notistack-snackbar").text
    # assert text=="با موفقیت تایید شد"



def test_not_reject_request():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(1)
    user0 =  driver.find_element("id" , ":r0:")
    user0.send_keys("sajjad")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("asdf@1234")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath", "//p[text()='خیر']").click()
    sleep(2)
    # text=driver.find_element("id","notistack-snackbar").text
    # assert text=="با موفقیت رد شد"

def test_approve_license_request_by_setad():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(2)
    user0 =  driver.find_element("id" , ":r0:")
    user0.send_keys("mohsen-setad-manager")
    passw0 = driver.find_element("id" , ":r1:")
    passw0.send_keys("qazwsx12")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath","//p[text()='لیست درخواست های مجوز']").click()
    sleep(1)
    driver.find_element("xpath" , "//p[text()='تائید']").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='بله']").click()
    sleep(1)
    toast = driver.find_element("css selector", ".SnackbarContainer-bottom").text
    assert toast == "با موفقیت تایید شد"
    sleep(3)

def test_reject_license_request_by_setad():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(2)
    user0 = driver.find_element("id", ":r0:")
    user0.send_keys("mohsen-setad-manager")
    passw0 = driver.find_element("id", ":r1:")
    passw0.send_keys("qazwsx12")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath", "//p[text()='لیست درخواست های مجوز']").click()
    sleep(1)
    driver.find_element("xpath", "//p[text()='تائید']").click()
    sleep(1)
    driver.find_element("xpath", "//p[text()='بله']").click()
    sleep(1)
    toast = driver.find_element("css selector", ".SnackbarContainer-bottom").text
    assert toast == "با موفقیت تایید شد"
    sleep(3)






def add_new_manager_by_setad():
    driver.get("https://dev-dashboard.hnaya.app/signin")
    driver.maximize_window()
    sleep(2)
    user0 = driver.find_element("id", ":r0:")
    user0.send_keys("mohsen-setad-manager")
    passw0 = driver.find_element("id", ":r1:")
    passw0.send_keys("qazwsx12")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath", "//p[text()='لیست منیجر های من']").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='لیست منیجر های من']").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='افزودن']").click()
    sleep(1)
    driver.find_element("name","name").send_keys(fake_name)
    driver.find_element("name","username").send_keys(fake_username)
    driver.find_element("name","password").send_keys("TEST")
    driver.find_element("name","email").send_keys("mostafakashi813@gmail.com")
    sleep(1)
    driver.find_element("xpath","//p[text()='MASTER']").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='تایید اطلاعات تکمیل شده']").click()
    sleep(2)
    text=driver.find_element("id","notistack-snackbar").text
    assert text=="با موفقیت ثبت شد"
    sleep(2)
    driver.find_element("xpath","//div[contains(@class,'MuiSelect-select MuiTablePagination-select')]").click()
    sleep(1)
    driver.find_element("xpath","//li[text()='همه']").click()
    sleep(1)
    dom = driver.page_source
    assert fake_username in dom
    sleep(4)



add_new_manager_by_setad()
