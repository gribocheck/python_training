# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import Date


def test_add_address(app):
    app.session.login("admin", "secret")
    app.contact.add(
        Contact("test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                "test", "test", "test", "test", "test", "test", "test", "test"),
        Date("2", "January", "1999"), Date("2", "January", "2018"))
    app.session.logout()


def test_add_address_empty(app):
    app.session.login("admin", "secret")
    app.contact.add(Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
                    Date("", "-", ""), Date("", "-", ""))
    app.session.logout()
