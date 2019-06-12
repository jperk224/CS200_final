# Build a dictionary that contains the movie collection below. Hint: Combine movie title and director into a list.
# Since we'll be referencing movies primarily by year and dictionary keys must be unique,
# each year's collection of movies is a list containing all movies associated with that year
# Each individual movie is represented as a list containing the title and director

movie_collection = {
    2005: [['Munich', 'Steven Spielberg']],
    2006: [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']]
}

# Prompt the user for a single year and output the movie title(s) and director(s) from that year. Output N/A if the year is invalid.

# initialize user's year selection and max and min key values
min_year = min(list(movie_collection.keys()))
max_year = max(list(movie_collection.keys()))
user_year = int(input('Enter a year between 2005 and 2006: \n'))
# while (user_year < min(list(movie_collection.keys()))) and (user_year > max(list(movie_collection.keys()))):
#     user_year = int(input('Enter a year between '))

if (user_year < min_year) or (user_year > max_year):
    print('N/A')
else:
    for film in movie_collection[user_year]:
        print('%s, %s' % (film[0], film[1]))

# Display a menu that enables a user to display the movies sorted by year, director, or movie title.
# Each option is represented by a single character.
# If an invalid character is entered, continue to prompt for a valid choice.
# The program ends when the user chooses the option to Quit

options_menu = 'MENU\n' \
               'Sort by:\n' \
               'y - Year\n' \
               'd - Director\n' \
               't - Movie Title\n' \
               'q - Quit'
print()
print(options_menu)

user_option = input('Choose an option: \n').lower().strip()
while user_option not in ['y', 'd', 't', 'q']:
    user_option = input('Choose an option: \n').lower().strip()
while user_option != 'q':
    # Implement the sort by year menu option
    # Year:
    #     Title, Director
    if user_option == 'y':
        year_list = list(movie_collection.keys())
        for year in year_list:
            print('%d:' % year)
            for film in movie_collection[year]:
                print('\t%s, %s' % (film[0], film[1]))
    # Implement the sort by director menu option
    # For directors with multiple films on the list, order their films by year.
    # Director:
    #    Title, Year
    if user_option == 'd':
        print(user_option)
    # implement the sort by title menu option
    # Title
    #    Director, Year
    if user_option == 't':
        print(user_option)
    user_option = input('Choose an option: \n').lower().strip()
