"""
Prints out all the melons in our inventory
"""

from melons import *

melon_names = return_melon_info()

for melon in melon_names:
    seedless = melon_names[melon]["seedless"]
    price = melon_names[melon]["price"]
    flesh_color = melon_names[melon]["flesh_color"]
    rind_color = melon_names[melon]["rind_color"]

    print melon.upper()
    print "  seedless: {}".format(seedless)
    print "  price: ${}".format(price)
    print "  flesh color: {}".format(flesh_color)
    print "  rind color: {}".format(rind_color)
