# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact("New contact"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact("testUpd_name", "testUpd_mName", "testUpd_lName", "testUpd_nName", "testUpd_title",
                      "testUpd_company","testUpd_address", "testUpd_hPhone", "testUpd_mPhone", "testUpd_wPhone",
                      "testUpd_fPhone", "testUpd_e1", "testUpd_e2", "testUpd_e3", "testUpd_homepage",
                      "testUpd_address2", "testUpd_home2", "testUpd_notes2", "5", "February", "2000", "5", "February",
                      "2019")
    contact.id = old_contact_list[index].id
    app.contact.modify_any(contact, index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
