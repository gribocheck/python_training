from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact("New contact"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
