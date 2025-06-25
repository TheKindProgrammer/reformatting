def reformatNumber(number):
    number = number.replace('-', '')
    number = number.replace(' ', '')

    lst = []
    while len(number) > 4:
        three_digits = number[0:3]
        lst.append(three_digits)
        lst.append('-')
        number = number[3:]

    if len(number) == 2:
        lst.append(number)

    if len(number) == 3:
        lst.append(number)

    if len(number) == 4:
        two_digits = number[0:2]
        lst.append(two_digits)
        lst.append('-')
        number = number[2:]
        lst.append(number)

    s = ''.join(lst)
    return s