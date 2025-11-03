names = input('Enter names (separated by space):')
print(names)
names_list = sorted(names.split())
print(names_list, type(names_list))
names_tuple = tuple(names_list)
print(names_tuple, type(names_tuple))

with open('names_data.txt', 'w') as output_file:
    output_file.write(f'Sorted list:{names_list}\n')
    output_file.write(f'tuple:{names_tuple}\n')

with open('names_data.txt', 'r') as input_file:
    file_names_sorted_list_line = input_file.readline()
    file_names_tuple_line = input_file.readline()
    print(file_names_sorted_list_line)
    print(file_names_tuple_line)
