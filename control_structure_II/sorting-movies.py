# The movie collection data for this program 
# has been stored in a separate file 
# for ease of use and data maintainability.

import movie_collection

# Define a function that prompts the user for a single year 
# and outputs the movie title(s) and director(s) for that year. 
# Loop until the user enters a valid year within the range.
# A while loop is used becasue the number of iterations is unknown.

def single_year_output(movie_collection:dict) -> str:
    '''
    Prompt the user for a year and output the associated movie collection.

    Keyword arguments:
    movie_collection -- a dict representing movie collections paired with unique years
    '''
    # initialize the max year, min year, and user's selected year.
    
    min_year = min(list(movie_collection.keys()))
    max_year = max(list(movie_collection.keys()))
    user_year = int(input('Enter a year between %d and %d:\n' % (min_year, max_year)))
    while (user_year < min(list(movie_collection.keys()))) or (user_year > max(list(movie_collection.keys()))):
        user_year = int(input('That is not a valid entry.  Enter a year between %d and %d:\n' % (min_year, max_year)))
    
    # Find the list of movies for the given year.
    # Loop through the list to print the title and director for each movie.
    # A for loop is used beacuse the length of the list dict value 
    # dictates the number of iterations.

    for film in movie_collection[user_year]:
        print('%s, %s' % (film[0], film[1]))
    print()

# Define a function to display a menu that 
# enables the user to display the movies sorted by year, director, or movie title.
# Each option is represented by a single character.
# Continue to prompt the user for a valid choice if the first provided is invalid.
# A while loop is used becasue the number of iterations is unknown.
# The program ends when the user chooses the option to quit.

def menu() -> list:
    '''
    Render a menu of options for the user and return a list containing the menu and action characters
    '''
    options_menu = 'MENU\n' \
                'Sort by:\n' \
                'y - Year\n' \
                'd - Director\n' \
                't - Movie title\n' \
                'q - Quit\n'
    print(options_menu)
    
    # Return a list of letter options to be used as input validation for the main program.
    # Separate the options menu into a list of strings and use
    # conditional logic to add only the single char menu options
    # to the list being returned for main program iteration.
    # This allows the menu to be modifed in future versions
    # without affecting the main program.
    # This approach assumes the menu format is adhered to --> single-char - action
    
    options_list = options_menu.split()
    option_letters = []

    # A for loop is used becasue the length of the options list built from the
    # menu string dictates the number of iterations.

    for string in options_list:
        if((len(string) > 1) or string == '-'):
            continue
        else:
            option_letters.append(string)
    return([options_menu, option_letters])

# Define a function to render movie collections by year.

def render_by_year(year_list:list, movie_collection:dict) -> str:
    '''
    Render the movie collection grouped and ordered by year

    Keyword arguments:
    year_list -- a list representing all unique years in the movie collection
    movie_collection -- a dict representing movie collections paired with unique year keys
    '''
    # Implement the sort by year menu option.
        # Year:
        #     Title, Director
    # For loops are used because the data structure defines the number of iterations,
    # as the global variable year_list has a fixed length.
    # Sort the list of years to ensure output is in chronological order.
    
    year_list.sort()
    for year in year_list:
        print('%d:' % year)
        for film in movie_collection[year]:
            print('\t%s, %s' % (film[0], film[1]))
        print()

# Define a function to render movie collections by director.

def render_by_director(year_list:list, movie_list:list, movie_collection:dict) -> str:
    '''
    Render the movie collection grouped by director and ordered by year

    Keyword arguments:
    year_list -- a list representing all unique years in the movie collection
    movie_list -- a list representing movie lists containing title and director
    movie_collection -- a dict representing movie collections paired with unique year keys
    '''
    # Implement the sort by director menu option.
    # For directors with multiple films on the list, order their films by year.
        # Director:
        #    Title, Year
    # For loops are used because the data structures
    # for the function arguments define the number of iterations.

    # initialize the list of movie directors to iterate over
    
    directors_list = []
    
    # Sort the list of years to ensure output is in chronological order.
    
    year_list.sort()
    
    for year_collection in movie_list:
        for film in year_collection:
            directors_list.append(film[1])

    # Converting the resulting list to a set ensures only unique elements for director names.  
    # The set is then converted back to a list for subsequent iteration.

    directors_list = list(set(directors_list))       

    # Sort the list of directors to ensure output is in alphabetical order.

    directors_list.sort()

    # Nested for loops are used here.
    # For each director, iterate over the list of years.
    # For each year, iterate over the movie collection associated with that year
    # to see if there is a film directed by the main iteration's director.
    # If a match is found, render the movie and year.

    for director in directors_list:
        print('%s:' % director)
        for year in year_list:
            for film in movie_collection[year]:
                if (film[1] == director):
                    print('\t%s, %d' % (film[0], year))
        print()

# Define a function to render movie collections by title.

def render_by_title(year_list:list, movie_list:list, movie_collection:dict) -> str:
    '''
    Render the movie collection by title, ordered alphabetically

    Keyword arguments:
    year_list -- a list representing all unique years in the movie collection
    movie_list -- a list representing movie lists containing title and director
    movie_collection -- a dict representing movie collections paired with unique year keys
    '''
    # Implement the sort by title menu option.
    # Title:
    #    Director, Year
    # For loops are used because the data structure defines the number of iterations.

    # Initialize the list of movie titles to iterate over.

    title_list = []

    # In the main program, movie_list is a list of nested list elements representing
    # the collection of movies for each year in the main dict the global list is derived from.
    # Iterate over the list.  For each iteration, further iterate over that year's 
    # list of movies to extract the title for rendering.  

    for year_collection in movie_list:
        for film in year_collection:
            title_list.append(film[0])
    
    # Sort the list of titles for alphabetical rendering.

    title_list.sort()

    # Nested for loops are used to render the appropriate data as output.
    # For each move title in the list of movie titles,
    # iterate over every year in the global list of years and
    # check if the movie colleciton for the given iteration's year
    # contains the movie title for the main iteration's title.

    for title in title_list:
        print('%s:' % title)
        for year in year_list:
            for film in movie_collection[year]:
                if (film[0] == title):
                    print('\t%s, %d' % (film[1], year))
        print()
   
# Only execute the main program if this is the main script run 
# and the script is not imported by another module

if __name__ == "__main__":
    
    # initialize global scope variables
    
    movie_collection = movie_collection.movie_collection
    year_list = list(movie_collection.keys())
    movie_list = list(movie_collection.values())

    single_year_output(movie_collection)
    options_list = menu()[1]
    user_option = input('Choose an option:\n').lower().strip()

    # Loop until the user selects a valid entry
    while user_option not in options_list:
        user_option = input('That is not a valid choice.  Choose an option:\n').lower().strip()

    # Loop until the user opts to quit
    while user_option != 'q':
        if user_option == 'y':
            render_by_year(year_list, movie_collection)
        if user_option == 'd':
            render_by_director(year_list, movie_list, movie_collection)
        if user_option == 't':
            render_by_title(year_list, movie_list, movie_collection)
        options_list = menu()[1]
        user_option = input('Choose an option:\n').lower().strip()
        while user_option not in options_list:
            user_option = input('That is not a valid choice.  Choose an option:\n').lower().strip()