# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_group_list = app.group.get_group_list()
    group = Group("second", "sdgfdsgt", "dsfgdfg")
    app.group.create(group)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(new_group_list, key=Group.id_or_max) == sorted(old_group_list, key=Group.id_or_max)


# def test_add_group_empty(app):
#     app.group.create(Group("", "", ""))

