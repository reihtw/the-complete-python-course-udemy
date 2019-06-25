list_movies = []

def add_movie():
    print('\n')
    name     = input('Enter the movie name: ').capitalize()
    director = input('Enter the director name: ').capitalize()
    year     = input('Enter the release date: ')

    dict_movies = {
        'name': name,
        'director': director,
        'year': year
    }

    list_movies.append(dict_movies)
    print('[*] Done!')
    print('\n')

def find_movie():
    find_by = input('What property of the movie are you looking for? ').lower() 
    looking_for = input('What are you searching for? ').capitalize

    movies = find_by_attribute(list_movies, looking_for, lambda x: x[find_by])

    if movies == []:
        print('[-] No results...')
        wait()
        return
    movies_list(movies)

    
        
def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    
    return found

    


#def search_name():
#    print('\n')
#    name = input('Enter the movie name that you want to search: ').capitalize()
#    for movie in list_movies:
#        if movie['name'] == name:
#            smc(movie)
#            break
#    else:
#        print('\n[-] The movie hasn\'t been found.\n')
#    wait()

#def search_director():
#    print('\n')
#    director = input('Enter the director name that you want to search: ').capitalize()
#    for movie in list_movies:
#        if movie['director'] == director:
#            smc(movie)
#            continue
#        else:
#            print('\n[-] The director hasn\'t been found.\n')
#    wait()

#def search_director_year():
#    print('\n')
#    director = input('Enter the director name that you want to search: ').capitalize()
#    year = int(input('Enter the year to see which are released in the year: '))
#    for movie in list_movies:
#        if movie['director'] == director and movie['year'] == year:
#            smc(movie)
#            continue
#        else:
#            print('\n[-] We didn\'t found movies by this director released in that year.\n')
#    wait()

#def search_year():
#    print('\n')
#    year = int(input('Enter the year to see which are realed in that year: '))
#    for movie in list_movies:
#        if movie['year'] == year:
#            smc(movie)
#            continue
#        else:
#            print('\nThere is no movie registred in this year.')
#    wait()

def smc(movie):
    print(f'''

---------------------------------------------------------
Name: {movie['name']}
Director: {movie['director']}
Year: {movie['year']}
---------------------------------------------------------

    ''')

def wait():
    input('Press enter to continue...')
    print('\n'*100)

def movies_list(movies_list):
    for movie in movies_list:
        smc(movie)
    wait()

def main():
    cmd = int(input('''
###########################
#    MILESTONE PROJECT    #
###########################

 1 > Add movie
 2 > Search a movie
 3 > List the movies
-1 > Exit

>>> '''))

    if cmd == 1:
        add_movie()
    elif cmd == 2:
        find_movie()
#        search_cmd = int(input('''
#
#1 > Search by name
#2 > Search by director
#3 > Search by year
#4 > Search by director and by year
#
#>>> '''))
#        if search_cmd == 1:
#            search_name()
#        elif search_cmd == 2:
#            search_director()
#        elif search_cmd == 3:
#            search_year()
#        elif search_cmd == 4:
#            search_director_year()
#        else:
#            return '[-] Invalid command'
    elif cmd == 3:
        movies_list(list_movies)
    elif cmd == -1:
        return '\n\nBye...\n\n'
    else:
        return '[-] Invalid command'

while True:
    run = main()
    if run == '\n\nBye...\n\n':
        break