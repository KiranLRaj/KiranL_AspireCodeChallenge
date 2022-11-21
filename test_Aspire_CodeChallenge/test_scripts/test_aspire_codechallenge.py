import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_Aspire_CodeChallenge.test_scripts.conftest import ChromeBrowserSetup

class Test_CodeChallenge:

    driver = ChromeBrowserSetup()
    driver.get("https://codechallenge.odoo.com")
    @pytest.mark.order(1)
    def test_codechallenge_TC1(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Email']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("user@codechallenge.app")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("@sp1r3app")
        self.driver.find_element(By.XPATH, "// button[text() = 'Log in']").click()
        # TC 1 completed - Logging In
        print("TC 1")
        print("Application opened and Logged in Successfully     *****************")
        self.driver.save_screenshot("TC1_Login.png")

    @pytest.mark.order(2)
    def test_codechallenge_TC2(self):
            element=self.driver.find_element(By.XPATH,"//*[text()='Inventory']/parent::a[@role='option']")
            self.driver.execute_script("arguments[0].click();", element)
            # TC 2 completed - Open Inventory
            print("STEP 2")
            print("Inventory opened     *****************")
            self.driver.save_screenshot("TC2_OpenInventory.png")
    @pytest.mark.order(3)
    def test_codechallenge_TC3(self):
        self.driver.find_element(By.XPATH,"//span[text()='Products']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Products']").click()
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Create')]").click()
        self.driver.find_element(By.XPATH,"//input[@name='name']").click()
        self.driver.find_element(By.XPATH, "//input[@name='name']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("KiranL_Aspire Code Challenge")
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
        # TC 3 completed - Navigate to Products and create a new Product
        print("TC 3")
        print("New Product created     *****************")
        time.sleep(3)
        self.driver.save_screenshot("TC3_CreateProduct.png")
    @pytest.mark.order(4)
    def test_codechallenge_TC4(self):
        element=self.driver.find_element(By.XPATH, "//span[contains(text(),'Update Quantity')]/..")
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.double_click().perform()
        self.driver.find_element(By.XPATH,"//button[@data-original-title='Create record']").click()
        self.driver.find_element(By.XPATH, "// input[ @ name = 'inventory_quantity']").click()
        self.driver.find_element(By.XPATH, "// input[ @ name = 'inventory_quantity']").clear()
        self.driver.find_element(By.XPATH, "// input[ @ name = 'inventory_quantity']").send_keys("30")
        self.driver.find_element(By.XPATH, "//button[@title='Save record']").click()
        # TC 4 completed - Update the product quantity to more than 10
        print("TC 4")
        print("Updated the product quantity to 30     *****************")
        self.driver.save_screenshot("TC4_UpdateQuantity.png")
    @pytest.mark.order(5)
    def test_codechallenge_TC5(self):
        self.driver.find_element(By.XPATH,"//a[@title='Home menu']").click()
        element = self.driver.find_element(By.XPATH, "//*[text()='Manufacturing']/parent::a[@role='option']")
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(By.XPATH, "//button[@data-original-title='Create record']").click()
        self.driver.find_element(By.XPATH, "//div[@name='product_id']/div/div/input").click()
        self.driver.find_element(By.XPATH, "//div[@name='product_id']/div/div/input").clear()
        self.driver.find_element(By.XPATH, "//div[@name='product_id']/div/div/input").send_keys("KiranL_Aspire Code Challenge")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Confirm']/..").click()
        # TC 5 and 6 completed - Navigate to Manufacturing feature and created a new MO for the product we created.
        print("TC 5 and 6")
        print("Navigated to the Manufacturing feature and created a new MO for the product we created before     *****************")
        time.sleep(2)
        self.driver.save_screenshot("TC6_CreateNewMO.png")
    @pytest.mark.order(6)
    def test_codechallenge_TC6(self):
        self.driver.find_element(By.XPATH,"(//span[contains(text(),'Mark as Done')]/..)[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Ok']").click()
        self.driver.find_element(By.XPATH,"//span[text()='Apply']/..").click()
        # Step 7 completed - Update status to Done
        print("TC 7")
        print("Marked the status to Done     *****************")
        self.driver.save_screenshot("TC7_Change_Status_Done.png")
    @pytest.mark.order(7)
    def test_codechallenge_TC7(self):
        if len(self.driver.find_elements(By.XPATH,"// *[text() = 'Production Order created']"))>0:
            print("Validation of Manufacturing Order(MO) creation is Successful")
        else:
            print("New Manufacturing Order creation failed")

        if len(self.driver.find_elements(By.XPATH,"//*[@title='Changed']/following-sibling::div[text()='Confirmed']"))>0:
            print("Validation of MO status change to 'COMFIRMED' is Successful")
        else:
            print("MO Status change to CONFIRMED failed")

        if len(self.driver.find_elements(By.XPATH,"//*[@title='Changed']/following-sibling::div[text()='Done']"))>0:
            print("Validation of MO status change to 'DONE' is Successful")
        else:
            print("MO Status change to DONE failed")

        print("TC 8")
        print("Validating Manufacturing Order details     *****************")
        self.driver.save_screenshot("TC8_Validation.png")




