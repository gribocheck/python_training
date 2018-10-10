# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact("New contact"))
    app.contact.modify_first(
        Contact("testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd",
                "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd",
                "5", "February", "2000", "5", "February", "2019"))
