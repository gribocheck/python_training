# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group("second", "sdgfdsgt", "dsfgdfg"))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)


# def test_add_group_empty(app):
#     app.group.create(Group("", "", ""))

