def reverse_string(text):
    """Returns the string in reverse order."""
    return text[::-1]

def alternate_caps(text):
    """Returns the string with alternating capital letters."""
    return "".join(char.upper() if idx % 2 == 0 else char.lower() for idx, char in enumerate(text))