# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add(
        Contact("test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                "test", "test", "test", "test", "test", "test", "test", "test",
                "2", "January", "1999", "2", "January", "2018"))
    app.session.logout()


def test_add_contact_empty(app):
    app.contact.add(Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                    "", "-", "", "", "-", ""))
