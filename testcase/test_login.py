from utilities.readProperties import ReadConfig
import pytest
from selenium import webdriver
from utilities.Logging import LogGen

import time
from pom.loginpage import LoginPageObjectes

@pytest.mark.usefixtures("OnetimeSetup")
class Test_Login():
    baseurl=ReadConfig.getApplicationUrl()
    Username=ReadConfig.getUsername()
    PassWord=ReadConfig.getPassWord()
    Usernameinvalid="admin12345"
    PassWordinvalid="admin123456"
    loggen=LogGen.loggen()

    @pytest.fixture(autouse=True)
    def driversetup(self,OnetimeSetup):
        self.driver=self.value

    def test_homepage_validate(self):
        self.loggen.info('###############startedt the home page test########')
        self.driver=self.value
        self.driver.get(self.baseurl)
        if self.driver.title=="OrangeHRM":
            assert True==True
        else:
            assert  True==False
            self.loggen.error('### asertion is failed')

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




