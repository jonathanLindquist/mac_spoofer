from textwrap import wrap
import random

stringAddress = ""
for x in range(12):
    stringAddress += hex(random.randint(1, 15)).strip('0x')

arrayAddress = wrap(stringAddress, 2)

address = ":".join(arrayAddress)

print(address)
