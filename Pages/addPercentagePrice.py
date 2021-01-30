from selenium.webdriver.support.ui import Select


class AddPercentagePriceField():

    def __init__(self, driver):
        self.driver = driver

        self.reset_to_defaults_button_name = "reset_fields"
        self.add_field_button_xpath = "//*[@id=\"thwepo_product_fields\"]/thead/tr[1]/th[1]/button[1]"
        self.field_name_textbox_xpath = "//*[@id=\"thwepo_field_form\"]/div[1]/div/table[1]/tbody/tr[2]/td[3]/input"
        self.field_title_textbox_xpath = "//*[@id=\"thwepo_field_form\"]/div[1]/div/table[2]/tbody/tr[1]/td[3]/input"
        self.price_details_tab_xpath = "//*[@id=\"thwepo_field_form_pp\"]/div/div/div/div/div/aside/ul/li[4]"
        self.price_type_select_xpath ="//*[@id=\"thwepo_field_form\"]/div[4]/div/table/tbody/tr[1]/td[3]/select"
        self.price_percentage_value_xpath = "//*[@id=\"thwepo_field_form\"]/div[4]/div/table/tbody/tr[2]/td[3]/input[1]"
        self.create_field_button_xpath = "//*[@id=\"thwepo_field_form_pp\"]/div/div/div/div/div/footer/div/button[1]/span"

    def create_percentage_price_field(self, field_name, field_title, price):
        self.driver.find_element_by_name(self.reset_to_defaults_button_name).click()
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

        self.driver.find_element_by_xpath(self.add_field_button_xpath).click()
        self.driver.find_element_by_xpath(self.field_name_textbox_xpath).send_keys(field_name)
        self.driver.find_element_by_xpath(self.field_title_textbox_xpath).send_keys(field_title)
        self.driver.find_element_by_xpath(self.price_details_tab_xpath).click()
        self.select_price_type_value_xpath = Select(self.driver.find_element_by_xpath(self.price_type_select_xpath))
        self.select_price_type_value_xpath.select_by_value("percentage")
        self.driver.find_element_by_xpath(self.price_percentage_value_xpath).send_keys(price)
        self.driver.find_element_by_xpath(self.create_field_button_xpath).click()