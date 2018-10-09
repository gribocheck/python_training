# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("second", "sdgfdsgt", "dsfgdfg"))


def test_add_group_empty(app):
    app.group.create(Group("", "", ""))

