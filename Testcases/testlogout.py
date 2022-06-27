import time
import pytest
from self import self

from Commonfunction.Login import loginfunction
from Pageobjects.LoginPage import LoginPage
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen


class Test_002_Logout(loginfunction):
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_logout(self, setup):
        data = loginfunction.login(self, setup)
        self.lp = LoginPage(data)
        self.lp.dropdown()
        time.sleep(2)
        self.lp.clicklogout()
        title = data.title
        print("the title is ", title)
        if title == "Infoquick - Login":
            data.save_screenshot("/Users/ticvictech/PycharmProjects/IBS-Automation/Screenshots/Logout/Pass_Logout.png")
            print("Logout success")
        else:
            data.save_screenshot("/Users/ticvictech/PycharmProjects/IBS-Automation/Screenshots/Logout/Fail_Logout.png")
            print("Logout failed")







