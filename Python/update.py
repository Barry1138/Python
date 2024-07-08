text = 'The political slogan "Congress shall make no law abriging the Freedom of Production and Trade."\n'
text = 'is from Atlas Shrugged.'

with open('update.txt', 'w') as file:
    file.write(text)
    print('\nFile Now Closed?:', file.closed)

    print('File Now Closed?:', file.closed)

with open('update.txt', 'r+') as file:
    text = file.read()
    print('\nString:', text)

    print('\nPostion In File Now:', file.tell())
    position = file.seek(33)
    print('Position In File Now:', file.tell())

    file.write('Competition')

    file.seek(61)
    file.write('the tombstone of Ayn Rand.')

    file.seek(0)
    text = file.read()
    print('\nString:', text)
