# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_data(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="")] + \
            [Group(name=random_data("name", 10), header=random_data("header", 20))
             for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_group_list = app.group.get_group_list()
    app.group.create(group)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(new_group_list, key=Group.id_or_max) == sorted(old_group_list, key=Group.id_or_max)



