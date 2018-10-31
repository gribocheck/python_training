from random import random

from selenium.webdriver.support.select import Select

from model.contact import Contact
import re
from random import randrange


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
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = cells[1].text
                name = cells[2].text
                address = cells[3].text
                emails = cells[4].text
                phones = cells[5].text
                self.contacts_cache.append(Contact(name=name, lastname=last_name, id=id,
                                                   address=address, all_emails=emails,
                                                   all_phones=phones))
        return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name=firstname, lastname=lastname, id=id,
                       address=address, home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone,
                       email_1=email1, email_2=email2, email_3=email3, secondary_home=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        content = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", content).group(1)
        work_phone = re.search("W: (.*)", content).group(1)
        mobile_phone = re.search("M: (.*)", content).group(1)
        secondary_phone = re.search("P: (.*)", content).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone,
                       secondary_home=secondary_phone)

    def get_random_contact_index(self, list_of_contacts):
        random_index = randrange(len(list_of_contacts))
        return random_index

    def merge_edit_phones_as_on_main(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.work_phone, contact.mobile_phone,
                                            contact.secondary_home]))))

    def merge_edit_emails_as_on_main(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email_1, contact.email_2, contact.email_3]))))

    def clear(self, str):
        return re.sub("[() -]", "", str)





