# unique_numbers_list.py
# Program to add unique numbers to a list.
# It does not allow duplicate numbers and lets the user decide whether to continue.

numbers = []

while True:
    n = int(input('Enter a number: '))
    
    if n not in numbers:
        numbers.append(n)
        print('Number added successfully!')
    else:
        print('ERROR! Number already added.')

    continue_input = input('Do you want to continue? [Y/N] ').strip().upper()
    
    while continue_input not in ('Y', 'N'):
        continue_input = input('Invalid option. Do you want to continue? [Y/N] ').strip().upper()
    
    if continue_input == 'N':
        break

print('-=' * 30)
print(f'You entered the values: {sorted(numbers)}')