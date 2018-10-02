from selenium import webdriver
from fixture.helper import Helper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.helper = Helper(self)

    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        wd = self.wd
        wd.quit()