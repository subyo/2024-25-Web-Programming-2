from selenium import webdriver # type: ignore

driver=webdriver.Chrome()
driver.get("http//example.com/login")

username_input = driver.find_element_by_id("username")
password_input =driver.find_elemennt_by_id("password")
sumbit_button =driver.find_element_by_id("sumbit")
 
username_input.send_keys("user123")
password_input.send_keys("pass123")
sumbit_button.click()

assert "Profile" in driver.title 
driver.quit()