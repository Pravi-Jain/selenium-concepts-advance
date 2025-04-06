from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

serv_obj = Service("C:\Drivers\msedgedriver.exe")

ops = Options()
ops.add_experimental_option(name="detach", value=True)

driver = webdriver.Edge(service=serv_obj, options=ops)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#input Boxes
driver.find_element(By.ID,"name").send_keys("ravi")
driver.find_element(By.XPATH, "//*[@class='form-control' and @placeholder='Enter EMail']").send_keys("rav@gmail.com")
driver.find_element(By.ID,"phone").send_keys("9900990099")
driver.find_element(By.XPATH,"//*[@id='textarea']").send_keys("address")

#Radio Buttons
driver.find_element(By.XPATH,"//*[@id='male']").click()

#checkboxes only Sunday and Friday
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
for ele in checkboxes:
    weekname=ele.get_attribute('id')
    if weekname=='sunday' or weekname=='friday':
        ele.click()

#dynamic button
button=driver.find_element(By.XPATH,"//button[contains(@name,'st')]")
print(button.text)
button.click()
print(button.text)

