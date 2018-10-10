from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact("New contact"))
    app.contact.delete_first_contact()
