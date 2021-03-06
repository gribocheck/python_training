import random
import string
import os.path
import getopt
import sys
import jsonpickle

from model.contact import Contact

try:
    opts, arg = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_data(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(name="", middle_name="", lastname="", nickname="", home_phone="", mobile_phone="", work_phone="")] + \
            [Contact(name=random_data("name", 10), lastname=random_data("lastname", 20), home_phone=random_data("+", 7),
                     work_phone=random_data("+", 7), email_1=random_data("mail-1", 7), email_2=random_data("mail-1", 7))
             for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(test_data))
