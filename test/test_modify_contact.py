# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import Date


def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first(
        Contact("testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd",
                "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd", "testUpd"),
        Date("5", "February", "2000"), Date("5", "February", "2019"))
    app.session.logout()

