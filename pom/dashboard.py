# all the objects is dashboard
class dashboardobjects():
    adminlink_xpath="//*[@id='menu_admin_viewAdminModule']/b"
    user_management_xpath="//*[@id='menu_admin_UserManagement']"
    users_xpath="//*[@id='menu_admin_viewSystemUsers']"
    PIM_xapth="//*[@id='menu_pim_viewPimModule']/b"
    leave_xapth="//*[@id='menu_leave_viewLeaveModule']/b"

    def __init__(self, driver):
        self.driver=driver

    def click_adminlink(self):
        self.driver.find_element_by_xpath(self.adminlink_xpath).click()
    def usermanagement(self):
        self.driver.find_element_by_xpath(self.user_management_xpath).click()
    def user_add(self):
        self.driver.find_element_by_xpath(self.users_xpath).click()
    def pim(self):
        self.driver.find_element_by_xpath(self.PIM_xapth).click()
    def leave(self):
        self.driver.find_element_by_xpath(self.leave_xapth).click()

