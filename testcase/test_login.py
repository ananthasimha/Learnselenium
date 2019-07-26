from utilities.readProperties import ReadConfig
import pytest
from selenium import webdriver

import time
from pom.loginpage import LoginPageObjectes

@pytest.mark.usefixtures("OnetimeSetup")
class Test_Login():
    baseurl=ReadConfig.getApplicationUrl()
    Username=ReadConfig.getUsername()
    PassWord=ReadConfig.getPassWord()
    Usernameinvalid="admin12345"
    PassWordinvalid="admin123456"

    @pytest.fixture(autouse=True)
    def driversetup(self,OnetimeSetup):
        self.driver=self.value

    def test_homepage_validate(self):
        self.driver=self.value
        self.driver.get(self.baseurl)
        assert self.driver.title=="OrangeHRM"
        self.driver.close()

    def test_Loginwithvaliddata(self,):
        self.driver.get(self.baseurl)
        self.login=LoginPageObjectes(self.driver)
        self.login.setUsername(self.Username)
        self.login.setPassWord(self.PassWord)
        self.login.ClickLogin()
    def test_Loginerror(self):
        self.driver.get(self.baseurl)
        self.login = LoginPageObjectes(self.driver)
        self.login.setUsername(self.Usernameinvalid)
        self.login.setPassWord(self.PassWordinvalid)
        self.login.ClickLogin()
        time.sleep(2)
        message=self.driver.find_element_by_xpath("//*[@id='spanMessage']").text
        assert message=="Invalid credentials"




