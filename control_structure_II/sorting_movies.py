# Build a dictionary that contains the movie collection below. Hint: Combine movie title and director into a list.
# Since we'll be referencing movies primarily by year and dictionary keys must be unique,
# each year's collection of movies is a list containing all movies associated with that year
# Each individual movie is represented as a list containing the title and director

movie_collection = {
    2005: [['Munich', 'Steven Spielberg']],
    2006: [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
    2007: [['Into the Wild', 'Sean Penn']],
    2008: [['The Dark Knight', 'Christopher Nolan']],
    2009: [['Mary and Max', 'Adam Elliot']],
    2010: [['The King\'s Speech', 'Tom Hooper']],
    2011: [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
    2012: [['Argo', 'Ben Affleck']],
    2013: [['12 Years a Slave', 'Steve McQueen']],
    2014: [['Birdman', 'Alejandro G. Inarritu']],
    2015: [['Spotlight', 'Tom McCarthy']],
    2016: [['The BFG', 'Steven Spielberg']]
}

# Prompt the user for a single year and output the movie title(s) and director(s) from that year. Output N/A if the year is invalid.

# initialize user's year selection and max and min key values
min_year = min(list(movie_collection.keys()))
max_year = max(list(movie_collection.keys()))
user_year = int(input('Enter a year between 2005 and 2016:\n'))
# while (user_year < min(list(movie_collection.keys()))) and (user_year > max(list(movie_collection.keys()))):
#     user_year = int(input('Enter a year between '))

if (user_year < min_year) or (user_year > max_year):
    print('N/A')
else:
    for film in movie_collection[user_year]:
        print('%s, %s' % (film[0], film[1]))
print()

# Display a menu that enables a user to display the movies sorted by year, director, or movie title.
# Each option is represented by a single character.
# If an invalid character is entered, continue to prompt for a valid choice.
# The program ends when the user chooses the option to Quit

options_menu = 'MENU\n' \
               'Sort by:\n' \
               'y - Year\n' \
               'd - Director\n' \
               't - Movie title\n' \
               'q - Quit\n'
# print()
print(options_menu)

# initialize loop scope variables
year_list = list(movie_collection.keys())
movie_list = list(movie_collection.values())
movie_tuples = list(movie_collection.items())

user_option = input('Choose an option:\n').lower().strip()
while user_option not in ['y', 'd', 't', 'q']:
    user_option = input('Choose an option:\n').lower().strip()
while user_option != 'q':
    # Implement the sort by year menu option
    # Year:
    #     Title, Director
    if user_option == 'y':
        for year in year_list:
            print('%d:' % year)
            for film in movie_collection[year]:
                print('\t%s, %s' % (film[0], film[1]))
            print()

    # Implement the sort by director menu option
    # For directors with multiple films on the list, order their films by year.
    # Director:
    #    Title, Year
    if user_option == 'd':
        # initialize the list of movie directors to iterate over
        directors_list = []
        year_list.sort()
        # year_list.reverse()
        for year_collection in movie_list:
            for film in year_collection:
                directors_list.append(film[1])
        directors_list = list(set(directors_list))       
        directors_list.sort()
        for director in directors_list:
            print('%s:' % director)
            for year in year_list:
                for film in movie_collection[year]:
                    if (film[1] == director):
                        print('\t%s, %d' % (film[0], year))
            print()

    # implement the sort by title menu option
    # Title:
    #    Director, Year
    if user_option == 't':
        # initialize the list of movie titles to iterate over
        title_list = []
        year_list.sort()
        year_list.reverse()
        for year_collection in movie_list:
            for film in year_collection:
                title_list.append(film[0])
        title_list.sort()
        for title in title_list:
            print('%s:' % title)
            for year in year_list:
                for film in movie_collection[year]:
                    if (film[0] == title):
                        print('\t%s, %d' % (film[1], year))
            print()
    print(options_menu)
    user_option = input('Choose an option:\n').lower().strip()