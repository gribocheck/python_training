# -*- coding: utf-8 -*-
from env.Lib.random import randrange
from model.group import Group


def test_modify_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="New group"))
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group = Group("modified2")
    group.id = old_group_list[index].id
    app.group.modify_any_group(group, index)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[index] = group
    assert sorted(new_group_list, key=Group.id_or_max) == sorted(old_group_list, key=Group.id_or_max)




