class GroupHelper:
    def __init__(self, helper, app):
        self.helper = helper
        self.app = app

    def create(self, group):
        wd = self.helper.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        #  fill in group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self):
        wd = self.helper.app.wd
        wd.find_element_by_link_text("groups").click()


