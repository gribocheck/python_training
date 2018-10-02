# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from date import Date
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address(app):
    app.login("admin", "secret")
    app.add_address_contact(Contact("test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                                    "test", "test", "test", "test", "test", "test", "test", "test"),
                            Date("2", "January", "1999"), Date("2", "January", "2018"))
    app.logout()


def test_add_address_empty(app):
    app.open_main_page()
    app.login("admin", "secret")
    app.add_address_contact(Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
                            Date("", "-", ""), Date("", "-", ""))
    app.logout()
