def is_even(num):
    """Returns True if the number is even, otherwise False."""
    return num % 2 == 0

def calculate_percent(value, total):
    """Returns the percentage of value relative to the total."""
    if total == 0:
        return 0
    return (value / total) * 100