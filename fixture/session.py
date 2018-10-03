
class SessionHelper:
    def __init__(self, helper, app):
        self.helper = helper
        self.app = app

    def logout(self):
        wd = self.helper.app.wd
        wd.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        wd = self.helper.app.wd
        self.helper.open_main_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()