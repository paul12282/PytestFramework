from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

baseURL = ReadConfig.getUrl()

def test_add_to_cart(setup):
    driver = setup
    driver.maximize_window()
    driver.get(baseURL)
    actions = ActionChains(driver)
    image_block = driver.find_element_by_xpath("//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]")
    add_button = driver.find_element_by_xpath(
        "//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[2]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView();", image_block)
    actions.move_to_element(image_block).move_to_element(add_button).click().perform()
    driver.close()