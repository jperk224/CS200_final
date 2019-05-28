# # Define a function to split the input string provided
# def split_string(user_input:str, split_on:str=' '):
#     '''
#     Return a list of substrings from the string provided

#     Keyword arguments:
#     user_input -- a non-empty string
#     split_on -- a non-empty string (default ' ')
#     '''
#     split_string = user_input.split(split_on)
#     return split_string

# Define a function to ensure each string in a split list is only one word
# Apply the strip method to each element in the pslit list to remove 
# leading and trailing whitespace
def multi_word_check(list:list):
    '''
    '''
    multi_word = False
    for string in list:
        array_check = []
        substring_split = string.split()
        for string in substring_split:
            strip_string = string.strip()
            array_check.append(strip_string)
        if len(array_check) > 1:
            multi_word = True
            break
    return multi_word

# Prompt the user for a string that contains two strings separated by a comma
user_input = input('Enter input string: ')

# Using a loop, extend the program to handle multiple lines of input. Continue until the user enters q to quit
while(user_input != 'q'):
    # Report an error if the input string does not contain a comma.
    # Continue to prompt until a valid string is entered.
    # If the input contains a comma, assume that the input also contains two strings.

    split_string = user_input.split(',')
    print(split_string)
    while(len(split_string) != 2):
        # check whether a comma exists in the string to allow desired splitting by comma
        if(len(split_string) <= 1):
            print('Error: No comma in string')
        # check for more than two substrings separated by commas
        elif(len(split_string) > 2):
            print('Error: Too many substrings separated by commas')
        
        user_input = input('Enter input string: ')
        split_string = user_input.split(',')

    # check for substrings with words not separated by commas
    # this ensures each substring has only one word
    while(multi_word_check(split_string)):
        print('Error: Commas separate strings containing more than a single word')
        user_input = input('Enter input string: ')
        split_string = user_input.split(',')

    # extract the two substrings from the input string and then remove any spaces
    first_word = split_string[0].split()[0]
    second_word = split_string[1].split()[0]

    print('First word:', first_word)
    print('Second word:', second_word)

    user_input = input('Enter input string: ')