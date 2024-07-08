'''
An excerpt from Animal Farm
'''

poem = 'All animals are equal\n'
poem += ', but some animals are\n'
poem += 'more equal than others.\n'

file = open('poem.txt', 'w')

file.write(poem)
file.close()

file = open('poem.txt', 'r')

for line in file:
    print(line, end = '')
file.close()

file = open('poem.txt', 'a')
file.write('(George Orwell)')
file.close()
