LEAP_YEAR = 'Високосный год'
REGULAR_YEAR = 'Обычный год'


def year_type(year):
    n = 4
    if year % 100 == 0:
        n *= 100

    if year % n == 0:
        return LEAP_YEAR

    return REGULAR_YEAR


year = int(input('Input year: '))
print(year_type(year))
