def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please enter ")

a = yes_or_no('question')
