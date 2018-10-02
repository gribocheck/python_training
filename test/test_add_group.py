# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.helper.session.login("admin", "secret")
    app.helper.group.create(Group("second", "sdgfdsgt", "dsfgdfg"))
    app.helper.session.logout()


def test_add_group_empty(app):
    app.helper.session.login("admin", "secret")
    app.helper.group.create(Group("", "", ""))
    app.helper.session.logout()

