# -*- coding: utf-8 -*-


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()




