from sys import maxsize


class Contact:
    def __init__(self, name=None, middle_name=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, all_phones=None, home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None,
                 all_emails=None, email_1=None, email_2=None, email_3=None, homepage=None, secondary_address=None,
                 secondary_home=None, secondary_notes=None, date=None, month=None, year=None, date2=None, month2=None,
                 year2=None, id=None):

        self.name = name
        self.middle_name = middle_name
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.all_phones = all_phones
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.all_emails = all_emails
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.secondary_address = secondary_address
        self.secondary_home = secondary_home
        self.secondary_notes = secondary_notes
        self.date = date
        self.month = month
        self.year = year
        self.date2 = date2
        self.month2 = month2
        self.year2 = year2
        self.id = id

    def __repr__(self):
        return "%s, %s %s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
