def get_weekday(current_weekday, days_ahead):
    """(int, int) -> int

Return which day of the week it will be days_ahead days from current_weekday.
current_weekday is the current day of the week and is in the range 1-7,
indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).
days_ahead is the number of days after today.

>>> get_weekday(3,2)    >>> get _weekday(1,0)
5                       1  
>>> get _weekday(6,1)   >>> get _weekday(4,7)
7                       4 
>>> get _weekday(7,1)   >>> get _weekday(7,72)
1                       2
"""
    return (current_weekday+days_ahead)%7
