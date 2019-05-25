# Prompt the user for a string that contains two strings separated by a comma
user_input = input('Enter input string: ')

# Using a loop, extend the program to handle multiple lines of input. Continue until the user enters q to quit
while(user_input != 'q'):
    # Report an error if the input string does not contain a comma.
    # Continue to prompt until a valid string is entered.
    # If the input contains a comma, assume that the input also contains two strings.

    split_string = user_input.split(',')
    while(len(split_string) < 2):
        # print(split_string)
        print('Error: No comma in string.')
        user_input = input('Enter input string: ')
        split_string = user_input.split(',')
    # print(split_string)

    # extract the two words from the input string and then remove any spaces
    first_word = split_string[0].split()[0]
    second_word = split_string[1].split()[0]

    print('First word:', first_word)
    print('Second word:', second_word)

    user_input = input('Enter input string: ')