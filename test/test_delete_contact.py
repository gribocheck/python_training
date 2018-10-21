from random import randrange

from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact("New contact"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete_contact_by_index(index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact_list
