from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
import time

class GoogleFormLocator:
    dropDownState = "//div[@role= 'option']//span[text()= 'Choose'][1]"
    txtAreaOffice = "//span[contains(text(), '{}')]//ancestor::div[@jscontroller]//input"
    btnSubmit = "//span[text() = 'Submit']"
    btnSwitchAccount = "//a[text()= 'Switch accounts']"
    currentAccount = "//a[text()= 'Switch accounts']/parent::div//span"

class GoogleFormPage(CommonFunction):
    def select_dropdown(self, field, value):
        self.click_element(By.XPATH, f"//span[contains(text(), '{field}')]//ancestor::div[@jscontroller]//span[text() = 'Choose']")
        self.click_element(By.XPATH, f"//span[contains(text(), '{field}')]//ancestor::div[@jscontroller]//div[@role= 'option' and @data-value = '{value}']")
        time.sleep(2)

    def enter_value_in_textbox(self, label, value):
        self.type_element(By.XPATH, f"//span[contains(text(), '{label}')]//ancestor::div[@jscontroller]//input", value)

    def submit_form(self):
        self.click_element(By.XPATH, GoogleFormLocator.btnSubmit)

    def submit_another_response(self):
        pass

    def get_all_accounts_displayed(self):
        pass

    def get_selected_google_account(self):
        pass

    def switch_account(self, email):
        self.click_element(By.XPATH, GoogleFormLocator.btnSwitchAccount)

