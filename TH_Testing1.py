import time

from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\tcm21\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://chgainz.trainheroic.com/app/signup/ch#/welcome")
driver.maximize_window()

driver.find_element_by_name("fullName").send_keys("Tyty Mueller")
driver.find_element_by_name("username").send_keys("TyTyMueller93")
driver.find_element_by_name("email").send_keys("tmueller1999@yahoo.com")
driver.find_element_by_name("password").send_keys("TytyMullet")
driver.find_element_by_name("phone").send_keys("6105134712")
driver.find_element_by_name("newOrgName").send_keys("Team Good Boiz")

time.sleep(3) # let the page load

driver.find_element_by_xpath("//button[contains(@class,'form-submit-button')]").click()

time.sleep(8) # let the page load

driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/button').click()

time.sleep(3)

driver.find_element_by_id("input_1").send_keys("Team Foxcatcher")
driver.find_element_by_id("input_2").send_keys("liteweight")

time.sleep(3)

driver.find_element_by_xpath("/html/body/div[6]/md-dialog/md-dialog-actions/button[2]").click()




