# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group("modified", "updated", "updated"))
    app.session.logout()




