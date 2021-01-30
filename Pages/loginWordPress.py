class LoginWordPress():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "user_login"
        self.password_textbox_id = "user_pass"
        self.submit_button_id = "wp-submit"

    def login_wordpress_dashboard(self, username, password):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        self.driver.find_element_by_id(self.submit_button_id).click()










