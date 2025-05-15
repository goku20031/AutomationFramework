from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
import time

class GoogleFormLocator:
    dropDownState = "//div[@role= 'option']//span[text()= 'Choose'][1]"
    txtAreaOffice = "//span[contains(text(), '{}')]//ancestor::div[@jscontroller]//input"
    btnSubmit = "//span[text() = 'Submit']"

class GoogleFormPage(CommonFunction):
    def select_dropdown(self, field, value):
        self.click_element(By.XPATH, f"//span[contains(text(), '{field}')]//ancestor::div[@jscontroller]//span[text() = 'Choose']")
        self.click_element(By.XPATH, f"//span[contains(text(), '{field}')]//ancestor::div[@jscontroller]//div[@role= 'option' and @data-value = '{value}']")
        time.sleep(2)