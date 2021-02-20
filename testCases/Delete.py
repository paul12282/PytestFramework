from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\Drivers\Chromedriver_32\chromedriver.exe")
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_id("search_query_top").clear()
driver.find_element_by_id("search_query_top").send_keys("dress")
driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
#title = driver.find_elements(By.CLASS_NAME, "product-name")
#results = [e.text for e in title]

results_title = driver.find_element_by_class_name("heading-counter").text
print(results_title[0])
if int(results_title[0]) > 0:
    print("Test passed")
else:
    print("Test failed")
driver.close()


#for x in results:
#    if "Dress" in x:
#        assert True
#    else:
#        assert False
