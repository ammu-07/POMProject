from selenium import webdriver
import unittest
import xlrd
from Pages.loginWordPress import LoginWordPress
from Pages.addField import AddField
from Pages.productPage import ProductPage

class FixedPrice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/ammuprakash/Desktop/Python/chromedriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://test.floopbox.com/wp-admin/edit.php?post_type=product&page=th_extra_product_options_pro")
        login = LoginWordPress(cls.driver)
        login.login_wordpress_dashboard("Ammu", "qa@india#")

    def test_01_fixed_price(self):
        driver = self.driver
        self.workbook = xlrd.open_workbook('/Users/ammuprakash/Downloads/Matrix.xlsx')
        self.sheet = self.workbook.sheet_by_index(0)

        for i in range(self.sheet.nrows):
            self.value_matrix = self.sheet.cell_value(i, 0)
            self.value_matrix_str = str(self.value_matrix)

            driver.get("https://test.floopbox.com/wp-admin/edit.php?post_type=product&page=th_extra_product_options_pro")
            add_field = AddField(driver)
            add_field.create_product_field("fixed_price_01", "Fixed Price 01", self.value_matrix_str)

            driver.get("https://test.floopbox.com/product/polo/")
            product_page = ProductPage(driver)
            product_page.product_price("Test value", self.value_matrix_str)

    @classmethod
    def tearDownClass(cls):
        print("Test completed successfully")
        cls.driver.close()
        cls.driver.quit()