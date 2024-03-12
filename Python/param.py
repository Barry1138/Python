def echo(user, lang, sys):
    print('User:', user, 'Language:', lang, 'Platform:', sys)

    echo('Barry', 'Python', 'Windows')

    echo(lang = 'Python', sys = 'Linux Mint', user = 'Anne')

    def mirror(user = 'Carole', lang = 'Bash'):
        print('\nUser:', user, 'Language:', lang)
        mirror()
        mirror(lang = 'JavaScript')
        mirror('Tony')
        mirror('Susan', 'HTML')
