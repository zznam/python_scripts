list = []
while True:
    word = input('Enter a number: ')
    if word == 'done':
        if (len(list) > 0):
            print('Maximum: ' + str(max(list)))
            print('Minimum: ' + str(min(list)))
        else:
            print('No item in list')
        break
    if (word.isnumeric()):
        list.append(word)
    else:
        print('It\'s not a number')
