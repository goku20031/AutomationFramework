from Shared.WebDriverBase import WebDriverBase
from Shared.CommonFunction import CommonFunction

class GoogleFormTest(WebDriverBase):

    def __init__(self):
        super().__init__()
        self.get_chrome_driver()
        self.open_url("google.com")

if __name__ == "__main__":
    obj = GoogleFormTest()
    print("ssss")