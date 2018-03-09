def yes_or_no(question):
    # It returns True or False, based on the user's response.
    while True:
        # There can also "y" or "n" answer.
        # It doesn't matter if upper- or lowercase.
        # There can be spaces before and after.
        answer = input(question).lower().strip()
        if answer == 'yes' or answer == 'y':
            return True
        elif answer == 'no' or answer == 'n':
            return False
        else:
            print('I do not understand! Reply "yes" or "no".')

if yes_or_no('Do you want to play a game? '):
    print('OK! But you have to program it first.')
else:
    print('It is a pity.')
