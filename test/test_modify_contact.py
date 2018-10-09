# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first(
        Contact("testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd",
                "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd",
                "5", "February", "2000", "5", "February", "2019"))
