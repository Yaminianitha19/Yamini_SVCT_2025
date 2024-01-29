def timeConversion(s):
    hour, minute, second = map(int, s[:-2].split(':'))
    period = s[-2:]

    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    return f'{hour:02}:{minute:02}:{second:02}'

# Sample Input
print(timeConversion("07:05:45PM"))  # Output: 19:05:45
