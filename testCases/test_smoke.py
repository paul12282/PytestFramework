from pageObjects.Login import LoginStep
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Random import RandomGen


class Test_homepage:
    baseURL = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    invalid_email = ReadConfig.getInvalidemail()
    password = ReadConfig.getPassword()
    search = ["dress", "t-shirt"]
    invalid_search = ["car" , "tree" , "phone" , "mouse" , "keyboard"]

    logger = LogGen.logGen()

    def test_login(self, setup):
        self.logger.info("**************** Test_homepage **********************")
        self.logger.info("**************** Login test initialized **********************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
        self.lp = LoginStep(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.driver.find_element_by_xpath(
                "//p[contains(text(),'Welcome to your account. Here you can manage all o')]").is_displayed():
            assert True
            self.logger.info("******************** Login test passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("******************** Login test failed *****************")
            assert False
        self.driver.close()

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
        self.lp = LoginStep(self.driver)
        self.lp.setEmail(self.invalid_email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.driver.find_element_by_xpath("//li[contains(text(),'Invalid email address.')]").is_displayed():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_invalid_login.png")
            assert False
        self.driver.close()

    def test_invalid_search(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.wrong_term = RandomGen(self.driver)
        self.driver.find_element_by_id("search_query_top").clear()
        self.wrong_term.invalid_gen(self.invalid_search)
        self.driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
        no_results = self.driver.find_element_by_class_name("heading-counter").text
        if int(no_results[0]) == 0:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_invalid_search.png")
            assert False
        self.driver.close()

    def test_valid_search(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.correct_term = RandomGen(self.driver)
        self.driver.find_element_by_id("search_query_top").clear()
        self.correct_term.valid_gen(self.search)
        self.driver.find_element_by_xpath("//header/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
        results = self.driver.find_element_by_class_name("heading-counter").text
        if int(results[0]) > 0:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_valid_search.png")
            assert False
        self.driver.close()