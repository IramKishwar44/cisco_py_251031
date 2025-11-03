sentence = input('Enter a sentence: ')
print(sentence)
words_list = sentence.split()
print(sentence, type(sentence))
words_tuple = tuple(word.upper() for word in words_list)
print(words_tuple, type(words_tuple))

with open('sentence_data.txt', 'w') as output_file:
    output_file.write(f'list:{words_list}\n')
    output_file.write(f'tuple:{words_tuple}\n')

with open('sentence_data.txt', 'r') as input_file:
    file_words_list_line = input_file.readline()
    file_words_tuple_line =  input_file.readline()
    print(file_words_list_line)
    print(file_words_tuple_line)
