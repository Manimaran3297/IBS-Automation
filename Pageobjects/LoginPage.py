import time
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_name = "username"
    textbox_password_name = "password"
    textbox_eye_icon_xpath = "//*[@id='login-form']/div[2]/span/span"
    checkbox_captcha_name = "robot"
    button_login_xpath = "//*[@id='login-form']/div[4]/button"
    button_logout_xpath = "/html/body/div[2]/div/div/ul/li[5]/span"
    link_Dropdown_xpath= "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/span"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        time.sleep(4)
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
        time.sleep(2)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.textbox_eye_icon_xpath).click()
        time.sleep(2)

    def clickCaptcha(self):
        self.driver.find_element(By.NAME, self.checkbox_captcha_name).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def dropdown(self):
        self.driver.find_element(By.XPATH, self.link_Dropdown_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
