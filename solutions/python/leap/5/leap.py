"""
    Determine whether a given year is a leap year.

    A year is a leap year if it is divisible by 4, except for years
    divisible by 100, which are only leap years if they are also
    divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Examples:
        >>> leap_year(2024)
        True
        >>> leap_year(1900)
        False
        >>> leap_year(2000)
        True
    """

def leap_year(year):
        
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)