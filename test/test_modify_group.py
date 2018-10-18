# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="New group"))
    old_group_list = app.group.get_group_list()
    app.group.modify_first_group(Group("modified2"))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)




