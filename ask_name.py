# -*- coding: cp1250 -*-

# This program is applicable for the Czech Republic
# where women names ends sometimes with "-ov�".

answer = input("What's your last name? ")

if answer.endswith('ov�') is True:
    print("You are a woman.")
else:
    print("You are a man.")
