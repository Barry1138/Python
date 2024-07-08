file = open('example.txt', 'w')

print('File Name:', file.name)
print('File Open Mode:', file.mode)

print('Readable:', file.readable())
print('Writable:', file.writable())

def get_status(f):
    if not f.closed:
        return 'Open'
    else:
        return 'Closed'

print('File Status:', get_status(file))
file.close()
print('\nFile Status:', get_status(file))
