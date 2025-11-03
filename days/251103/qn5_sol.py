numbers = input('Enter numbers (separated by space):')
print(numbers)
number_list = numbers.split()
print(number_list, type(number_list))

maximum = max(number_list)
print(maximum)
minimum = min(number_list)
print(minimum)

with open('minmax_data.txt', 'w') as output_file:
    output_file.write(f'Numbers: {number_list}\n')
    output_file.write(f'Maximum: {maximum}\n')
    output_file.write(f'Minimum: {minimum}\n')

with open('minmax_data.txt', 'r') as input_file:
    file_number_list_line = input_file.readline()
    file_maximum_line = input_file.readline()
    file_minimum_line = input_file.readline()
    print(file_number_list_line)
    print(file_maximum_line)
    print(file_minimum_line)
