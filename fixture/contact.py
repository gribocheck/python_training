from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        self.init_contact_creation()
        self.fill_primary_data_inputs(contact)
        self.submit_contact()
        self.contacts_cache = None

    def fill_primary_data_inputs(self, contact):
        self.fill_input("firstname", contact.name)
        self.fill_input("middlename", contact.middle_name)
        self.fill_input("lastname", contact.lastname)
        # fill nickname input
        self.fill_input("nickname", contact.nickname)

        # TODO change picking photo
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("C:\\fakepath\\IMG_20140307_133538.jpg")

        # fill title input
        self.fill_input("title", contact.title)
        # fill company input
        self.fill_input("company", contact.company)
        # fill company address input
        self.fill_input("address", contact.address)

        # fill home phone input
        self.fill_input("home", contact.home_phone)
        # fill mobile phone input
        self.fill_input("mobile", contact.mobile_phone)
        # fill wor phone input
        self.fill_input("work", contact.work_phone)
        # fill fax input
        self.fill_input("fax", contact.fax_phone)
        # fill email1 input
        self.fill_input("email", contact.email_1)
        # fill email2 input
        self.fill_input("email2", contact.email_2)
        # fill email3 input
        self.fill_input("email3", contact.email_3)
        # fill homepage input
        self.fill_input("homepage", contact.homepage)
        # add dates
        # self.pick_b_date(contact)
        # self.pick_a_date(contact)

        # wd.find_element_by_name("new_group").click()
        # Select(wd.find_element_by_name("new_group")).select_by_visible_text("first")
        # wd.find_element_by_name("new_group").click()

        # fill address input
        self.fill_input("address2", contact.secondary_address)
        # fill phone input
        self.fill_input("phone2", contact.secondary_home)
        # fill notes input
        self.fill_input("notes", contact.secondary_notes)

    def fill_input(self, input_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(input_name).click()
            wd.find_element_by_name(input_name).clear()
            wd.find_element_by_name(input_name).send_keys(value)

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def pick_a_date(self, contact):
        self.fill_date_input("aday", contact.date2)
        self.fill_date_input("amonth", contact.month2)
        self.fill_input("ayear", contact.year2)

    def fill_date_input(self, input_name, value):
        if value is not None:
            wd = self.app.wd
            wd.find_element_by_name(input_name).click()
            Select(wd.find_element_by_name(input_name)).select_by_visible_text(value)
            wd.find_element_by_name(input_name).click()

    def pick_b_date(self, contact):
        self.fill_date_input("bday", contact.date)
        self.fill_date_input("bmonth", contact.month)
        self.fill_input("byear", contact.year)

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def modify_first(self, contact):
        self.modify_any(contact, 0)

    def modify_any(self, contact, index):
        wd = self.app.wd
        self.app.open_main_page()
        # click edit icon
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_primary_data_inputs(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def count_contacts(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_main_page()
            self.contacts_cache = []
            elements = wd.find_elements_by_xpath("//tr[@name='entry']")
            for element in elements:
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = element.find_elements_by_tag_name("td")[1].text
                name = element.find_elements_by_tag_name("td")[2].text
                self.contacts_cache.append(Contact(name=name, lastname=last_name, id=id))
        return list(self.contacts_cache)


