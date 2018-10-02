# -*- coding: utf-8 -*-
import pytest

from application import Application
from group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("second", "sdgfdsgt", "dsfgdfg"))
    app.logout()


def test_add_group_empty(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

