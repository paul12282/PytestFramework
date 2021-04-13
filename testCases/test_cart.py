from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

baseURL = ReadConfig.getUrl()

def test_add_to_cart(setup):
    # adds the first item inside the cart, closes the pop-up and checks if the product is added to the top right list
    driver = setup
    driver.maximize_window()
    driver.get(baseURL)
    actions = ActionChains(driver)
    image_block = driver.find_element_by_xpath("//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]")
    add_button = driver.find_element_by_xpath(
        "//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[2]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView();", image_block)
    actions.move_to_element(image_block).move_to_element(add_button).click().perform()
    close_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cross")))
    close_icon.click()
    cart_status = driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView();", cart_status)
    actions.move_to_element(cart_status).perform()
    remove_icon = driver.find_element_by_xpath (
        "//header/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/dl[1]/dt[1]/span[1]/a[1]")
    if remove_icon.is_displayed():
        assert True
    else:
        assert False
    driver.close()

def test_add_remove_to_cart(setup):
    driver = setup
    driver.maximize_window()
    driver.get(baseURL)
    actions = ActionChains(driver)
    image_block = driver.find_element_by_xpath("//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]")
    add_button = driver.find_element_by_xpath(
        "//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[2]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView();", image_block)
    actions.move_to_element(image_block).move_to_element(add_button).click().perform()
    close_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cross")))
    close_icon.click()
    cart_status = driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]")
    remove_icon = driver.find_element_by_xpath(
        "//header/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/dl[1]/dt[1]/span[1]/a[1]")
    driver.execute_script("arguments[0].scrollIntoView();", cart_status)
    close_icon.click()
    actions.move_to_element(cart_status).move_to_element(remove_icon).click().perform()
    time.sleep(1)
    empty_status = driver.find_element_by_class_name("ajax_cart_no_product")
    if empty_status.is_displayed():
        assert True
    else:
        assert False