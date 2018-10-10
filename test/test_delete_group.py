# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="New group"))
    app.group.delete_first_group()




