class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.fixed_price_field_textbox_id = "fixed_price_01"
        self.extra_price_display_label_css_selector = "div.summary"
        self.extra_price_display_label_span_class = "extra-price"
        self.total_price_display_label_span_class = "total-price"
        self.extra_price_display_label_element_class = "woocommerce-Price-amount"
        self.add_to_cart_button_by_name = "add-to-cart"

    def product_price(self, price_value, price):

        self.driver.find_element_by_id(self.fixed_price_field_textbox_id).send_keys(price_value)
        self.driver.execute_script("jQuery('.thwepo-price-field').change()");
        self.driver.implicitly_wait(2)

        try:
            self.driver.find_element_by_id('dummy_value')
        except:
            print(" ")

        self.price_value = float(price)
        self.total_price_calculated = 20 + self.price_value
        self.product_price_label = self.driver.find_element_by_css_selector('div.summary').find_element_by_css_selector('p.price')
        self.product_price_label_value = self.product_price_label.text
        self.product_price_label_remove_suffix = self.product_price_label_value.replace("$", "")
        self.product_price_label_remove_comma = self.product_price_label_remove_suffix.replace(",", "")
        self.product_price_label_float = float(self.product_price_label_remove_comma)

        if self.product_price_label_float == self.total_price_calculated:
            print("Price label is updated successfully", self.product_price_label_float)

        else:
            print("Price label not updated:", self.total_price_display_remove_suffix_float)

        self.extra_price_display = self.driver.find_element_by_css_selector(self.extra_price_display_label_css_selector).find_element_by_class_name(self.extra_price_display_label_span_class).find_element_by_class_name(self.extra_price_display_label_element_class)
        self.extra_price_display_remove_suffix_value = self.extra_price_display.text
        self.extra_price_display_remove_suffix = self.extra_price_display_remove_suffix_value.replace("$", "")
        self.extra_price_display_remove_comma = self.extra_price_display_remove_suffix.replace(',', '')
        self.extra_price_display_remove_suffix_float = float(self.extra_price_display_remove_comma)

        if self.extra_price_display_remove_suffix_float == price:
            print("Extra product options price is displayed successfully:", self.extra_price_display_remove_suffix_float)

        else:
            print("Price not displayed")

        self.total_price_display = self.driver.find_element_by_css_selector(self.extra_price_display_label_css_selector).find_element_by_class_name(self.total_price_display_label_span_class).find_element_by_class_name(self.extra_price_display_label_element_class)
        self.total_price_display_remove_suffix_value = self.total_price_display.text
        self.total_price_display_remove_comma = self.total_price_display_remove_suffix_value.replace(',', '')
        self.total_price_display_remove_suffix = self.total_price_display_remove_comma.replace("$", "")
        self.total_price_display_remove_suffix_float = float(self.total_price_display_remove_suffix)

        if self.total_price_display_remove_suffix_float == self.total_price_calculated:
            print("Total price is updated successfully on Price table", self.total_price_display_remove_suffix_float)

        else:
            print("Price not calculated:", total_price_display_remove_suffix_float)