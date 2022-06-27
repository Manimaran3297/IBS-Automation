
import time
import pytest
from Commonfunction.Login import loginfunction
from Testcases.conftest import setup
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen
from selenium import webdriver


class Test_001_Login(loginfunction):
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        data = loginfunction.LaunchURL(self, setup)
        time.sleep(5)
        actual_title = data.title
        time.sleep(3)

        if actual_title == "Infoquick - Login":
            data.save_screenshot("/Users/ticvictech/PycharmProjects/IBS-Automation/Screenshots/Login/Homepage_Pass/Pass_homepagetitle.png")
            assert True
            data.close()
            self.logger.info("************* Home Page Title verification is passed *************")
        else:
            data.save_screenshot("/Users/ticvictech/PycharmProjects/IBS-Automation/Screenshots/Login/Homepage_Fail/Fail_homepagetitle.png")
            data.close()
            self.logger.info("********** Home Page Title verification is Failed ***************")
            assert False

    def test_login(self, setup):

        data = loginfunction.login(self, setup)
        time.sleep(5)
        title = data.title
        actual_title = data.title
        print("act_title --", actual_title)
        time.sleep(3)
        data.close()

        if actual_title != "Infoquick - System Resources":
            print("************** Login Page Verification successfully done ***************")
            print("Title Verified ", title)
            assert True
        else:
            self.logger.info("*************** Login Page URL is invalid ********************")
            print("*************** Login Page is not  ******************** ")
            assert False