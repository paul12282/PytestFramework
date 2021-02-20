class LoginStep:
    email_id="email"
    password_id="passwd"
    button_css="#SubmitLogin"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_css_selector(self.button_css).click()