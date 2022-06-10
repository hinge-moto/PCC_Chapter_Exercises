# May 23.2022

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    if last[:2] == 'mc':
        mc_last = 'Mc' + last[2:].title()
        full_name = f"{first.title()} {mc_last}"
        return full_name
    else:
        return full_name.title()
