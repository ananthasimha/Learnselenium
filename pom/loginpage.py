

# add in the Logon page locators
class LoginPageObjectes():
    UserName_Id="txtUsername"
    PassWord_Id="txtPassword"
    Login_Btn_Id="btnLogin"
    ForgotPassWord_xpath="//*[@id='forgotPasswordLink']/a"
    UserName_Id_invalid = "txtUsername"
    PassWord_Id_invalid = "txtPassword"
    errormessage="//*[@id='spanMessage']"
    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,Username):
        self.driver.find_element_by_id(self.UserName_Id).send_keys(Username)

    def setPassWord(self,PassWord):
        self.driver.find_element_by_id(self.PassWord_Id).send_keys(PassWord)

    def setUsernameinvalid(self,Usernameinvalid):
        self.driver.find_element_by_id(self.UserName_Id_invalid).send_keys(Usernameinvalid)

    def setPassWordinvalid(self,PassWordinvalid):
        self.driver.find_element_by_id(self.PassWord_Id_invalid).send_keys(PassWordinvalid)

    def ClickLogin(self):
        self.driver.find_element_by_id(self.Login_Btn_Id).click()
    def SetForgotPassword(self,ForgotPassword):
        self.driver.find_element_by_xpath(self.ForgotPassWord_xpath).click()
    def errormesage(self,message):
        message=self.driver.find_element_by_xpath(self.errormessage).text
        return message


