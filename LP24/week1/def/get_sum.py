def get_summ(one, two, delimiter=' '):
    str_one = str(one)
    str_two = str(two)
    str_main = str_one + delimiter + str_two
    return print(str_main.title())

print(get_summ('Learn', 'python'))
