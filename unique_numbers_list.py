numbers = []

while True:
    n = int(input('Enter a number: '))
    if n not in numbers:
        numbers.append(n)
        print('Number added successfully!')
    else:
        print('ERROR! Number already added.')

    continue_input = str(input('Do you want to continue? [Y/N] '))
    while continue_input not in 'YyNn':
        continue_input = str(input('Do you want to continue? [Y/N] '))
    
    if continue_input in 'Nn':
        break

numbers.sort()
print('-=' * 30)
print(f'You entered the values: {numbers}')