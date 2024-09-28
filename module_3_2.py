def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print()

print_params(b = 25)
print_params(c = [1, 2, 3])
print()

values_list = ['text', 7, True]
values_dict = {'a': 'first', 'b': 3.15, 'c': False}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2,42)