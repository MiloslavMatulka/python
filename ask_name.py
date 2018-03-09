# -*- coding: cp1250 -*-

# This program is applicable for the Czech Republic
# where women names ends sometimes with "-ová".

answer = input("What's your last name? ")

if answer.endswith('ová') is True:
    print("You are a woman.")
else:
    print("You are a man.")
