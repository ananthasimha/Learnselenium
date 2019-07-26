# validate the  all the tabs in the dash board
import pytest
from utilities.readProperties import ReadConfig
from pom.loginpage import LoginPageObjectes
from pom.dashboard import dashboardobjects
from selenium import webdriver
import time

@pytest.mark.usefixtures("OnetimeSetup")
class Test_Dashboard():
        baseurl = ReadConfig.getApplicationUrl()
        Username = ReadConfig.getUsername()
        PassWord = ReadConfig.getPassWord()

        @pytest.fixture(autouse=True)

        def driversetup(self, OnetimeSetup):
            self.driver = self.value
        @pytest.fixture()
        def setup(self):
            self.driver.get(self.baseurl)
            self.login = LoginPageObjectes(self.driver)
            self.login.setUsername(self.Username)
            self.login.setPassWord(self.PassWord)
            self.login.ClickLogin()
            time.sleep(3)
            yield
            self.driver.close()
        def test_validateadminmodule(self,setup):
            self.dash=dashboardobjects(self.driver)
            self.dash.click_adminlink()
            assert self.driver.current_url=="https://opensource-demo.orangehrmlive.com/index.php/admin/viewAdminModule"
        def test_validateemplist(self,setup):
            self.dash=dashboardobjects(self.driver)
            self.dash.pim()
            assert self.driver.current_url=="https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList"