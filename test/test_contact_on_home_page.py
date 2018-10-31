
def test_contact_on_home_and_edit_page(app):
    contact_list = app.contact.get_contact_list()
    random_index = app.contact.get_random_contact_index(contact_list)
    contact_from_home_page = contact_list[random_index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(random_index)
    contact_from_edit_page.all_emails = app.contact.merge_edit_emails_as_on_main(contact_from_edit_page)
    contact_from_edit_page.all_phones = app.contact.merge_edit_phones_as_on_main(contact_from_edit_page)
    assert contact_from_home_page == contact_from_edit_page

