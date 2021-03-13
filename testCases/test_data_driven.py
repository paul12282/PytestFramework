from pageObjects.Login import LoginStep
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time

baseURL = ReadConfig.getUrl()
path = ".//TestData/LoginData.xlsx"

def test_data_driven(setup):
    driver = setup
    driver.maximize_window()
    driver.get(baseURL)
    driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
    lp = LoginStep(driver)
    status = []

    rows = XLUtils.getRowCount(path, "Sheet1")
    for r in range(2, rows + 1):
        user = XLUtils.readData(path, "Sheet1", r, 1)
        password = XLUtils.readData(path, "Sheet1", r, 2)
        expected = XLUtils.readData(path, "Sheet1", r, 3)
        lp.setEmail(user)
        lp.setPassword(password)
        lp.clickLogin()
        time.sleep(3)
        act_title = driver.title
        exp_title = "Login - My Store"

        if act_title == exp_title:
            if expected == "Fail":
                status.append("Pass")
            elif expected == "Pass":
                status.append("Fail")
        elif act_title != exp_title:
            if expected == "Pass":
                status.append("Pass")
            elif expected == "Fail":
                status.append("Fail")

        if "Fail" not in status:
            assert True
        else:
            assert False
    driver.close()
