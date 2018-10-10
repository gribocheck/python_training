from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.wd.get("http://localhost/addressbook/group.php")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_main_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        wd = self.wd
        wd.quit()

    def is_valid(self):
        wd = self.wd
        try:
            wd.current_url()
            return True
        except:
            return False
