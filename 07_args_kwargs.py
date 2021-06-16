def print_args(var, *argv):
    print(var)
    for arg in argv:
        print(*argv)


print_args('a', 'b', 'c', 'd')


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value}')


print_kwargs(first_name='Jane', last_name='Doe')

jane_doe = {'first name': 'Jane', 'last name': 'Doe'}
print_kwargs(**jane_doe)    # Remember to add **