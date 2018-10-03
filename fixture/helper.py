from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Helper:
    def __init__(self, app):
        self.app = app
        self.session = SessionHelper(self, app)
        self.group = GroupHelper(self, app)
        self.contact = ContactHelper(self, app)

    def open_main_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        wd = self.app.wd
        wd.quit()