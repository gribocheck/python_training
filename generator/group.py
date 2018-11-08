from model.group import Group
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, arg = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_data(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="")] + \
            [Group(name=random_data("name", 10), header=random_data("header", 20))
             for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(test_data))
