def yes_or_no(question):
    """
    Returns True for input starting with y or N
    Returns False for input starting with n or N
    Repeat question when neither y nor n was input
    """
    reply = str(raw_input(question+' (y/n): ')).lower()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please enter ")

a = yes_or_no('Would you like to continue?')
