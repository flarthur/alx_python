#!/usr/bin/python3
""" Check """
from models.square import Square

sq = Square(12)
if sq is None:
    print("Can't create Square")
    exit(1)

for attribute in list(sq.__dict__.keys()):
    if "size" in attribute:
        print(
            "You are not allowed to add any new attribute for size: {}".format(
                attribute
            )
        )
        exit(1)

if sq.size != 12:
    print("Wrong size getter: {}".format(sq.size))
    exit(1)

sq.size = 5

if sq.size != 5:
    print("Wrong size getter: {}".format(sq.size))
    exit(1)

print("OK", end="")
