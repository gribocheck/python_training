from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.group_cache = None

    def fill_group_form(self, group):
        self.fill_input("group_name", group.name)
        self.fill_input("group_header", group.header)
        self.fill_input("group_footer", group.footer)

    def fill_input(self, input_name, input_value):
        if input_value is not None:
            wd = self.app.wd
            wd.find_element_by_name(input_name).click()
            wd.find_element_by_name(input_name).clear()
            wd.find_element_by_name(input_name).send_keys(input_value)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self, index):
        self.delete_group_by_index(index)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()
        # init group deletion
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def modify_first_group(self, group):
        self.modify_any_group(group, 0)

    def modify_any_group(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()
        # init group editing
        wd.find_element_by_name("edit").click()
        # fill in group form
        self.fill_group_form(group)
        # submit group editing
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def count_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_xpath("//span[@class='group']"):
                name = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=name, id=id))
        return self.group_cache




