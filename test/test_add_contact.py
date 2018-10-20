# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact("test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                "test", "test", "test", "test", "test", "test", "test", "test",
                "2", "January", "1999", "2", "January", "2018")
    app.contact.add(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


# def test_add_contact_empty(app):
#     app.contact.add(Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
#                     "", "-", "", "", "-", ""))