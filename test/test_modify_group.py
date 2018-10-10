# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify_first_group(Group("modified2"))




