def to_weird_case(string):
    list_of_letters = []

    for i in string.split(' '):
        list_of_letters.append(i)

    new_list = up_low(list_of_letters)
    new_string = ''.join(new_list)
    new_string = new_string[:-1]

    return new_string

def up_low(list_of_letters):
    n = 0
    space = " "
    new_list = []

    while n != len(list_of_letters):
        x = 0

        for i in list_of_letters[n]:
            if x % 2 == 0 or x == 0:
                i = i.upper()
                new_list.append(i)
            elif x % 2 != 0:
                i = i.lower()
                new_list.append(i)
            x += 1
        n += 1
        new_list.append(space)

    return new_list
