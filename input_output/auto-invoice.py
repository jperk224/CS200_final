# Import the inflect package to convert numerals into ordinals.
# This is used for the service_input function.
# You must install inflect prior to running.
# pip install inflect --user
# inflect.py is an external library that can be used to
# generate plurals, singular nouns, ordinals, indefinite articles, and convert numbers to words.
# https://pypi.org/project/inflect/

import inflect

# Assign an ordinal variable to an instance of inflect's engine class.
# The engine class contians several methods to convert numbers to words 
# and represent ordinality.
# The variable will be used to convert each service_input loop iteration's 
# int representation into its ordinal representation for readability 
# for the service selection output to the user.

ordinal = inflect.engine()

# A dict type is the best data type for the availabe services.  
# The dict yields an associative relationship between service and price.
# and allows for changing prices and adding services, as dicts are mutable.
# Floats are used for the dict values as
# they are the best data type for representing prices
# the dict below uses multiple lines and white space for readability

services = {
    'Oil change': 35.00,
    'Tire rotation': 19.00,
    'Car wash': 7.00,
    'Car wax': 12.00
}

# Declare a funciton to loop through the dict of services to output 
# a menu of automotive services and the corresponding cost of each service.
# A loop is used becasue the dict parameter can be modified
# and the data structure dictates the number of loop iterations.
# With dict modification, this loop will not need to change
# and will always reflect the current key-value pairs.

def service_menu(services:dict) -> str:
    '''
    Print interpolated strings for key:value pairs.

    Keyword arguments:
    services -- a non-empty dictionary with float or int values
    '''
    # Iterate over a view object of key-value tuples to print
    # a menu of available services.
    # A for loop is used because the dict data structure and 
    # resulting tuple view object dictates the number of iterations.
    for key, value in services.items():
        # print item -- price for each element in services dict.
        print('%s -- $%d' % (key, value))

# Prompt the user for services from the menu.
# A loop is used so the code can be easily modified
# to prompt for more or less services as needed in future versions. 
# The default is to prompt for input twice.

def service_input(services:dict, prompts:int=2) -> list:
    '''
    Return a list of elements representing the user input.

    Keyword arguments:
    services -- a non-empty dictionary
    prompts -- int to define the number of loop iterations (default 2)

    '''
    # Create an empty list to store loop iteration values.
    # This will be returned by the function to be used 
    # as input for subsequent functions.
    services_ordered = []

    # Iterate over the number of prompts to capture user input.
    # A for loop is used beacues the number of iterations is known (i.e. prompts parameter)
    
    for num in range(1, (prompts + 1)):
        
        # Use the ordinal method to convert num to ordinal (e.g. 1 -> 1st).
        # Use the number_to_words method to convert the ordinal to word (e.g. 1st -> first).
        # The while loop ensures the user enters a valid service from the service menu.
        # A while loop is used because the number of iterations is unknown.
        
        valid_entry = False
        while(not valid_entry):
            service_ordered = input('Select %s service (Enter \'-\' for no service): \n' % (ordinal.number_to_words(ordinal.ordinal(num))))
            if service_ordered in services:
                services_ordered.append(service_ordered)
                valid_entry = True
            elif (service_ordered == '-'):
                services_ordered.append('No service')
                valid_entry = True
            else:
                print('That is not a valid entry, please try again.')

    return services_ordered

# Loop thorugh the list of services ordered and output the service and price.
# A for loop is used beacuse the lenght of the list paramenter dictates the number of iterations.

def service_output(list:list, services:dict) -> str:
    '''
    Print interpolated strings for list elements

    Keyword arguments:
    list -- a non-empty list
    services -- a non-empty dictionary with float or int values

    '''
    for num in range(0, len(list)):
        if (list[num] == 'No service'):
            print('Service %d: No service' % (num + 1))
        else:
            print('Service %d: %s, $%d' % ((num + 1), list[num], services[list[num]]))

# Print the total cost of the services selected.
# Loop thorugh the list of services ordered and sum the associated prices.
# A for loop is used beacuse the lenght of the list paramenter dictates the number of iterations.

def invoice_total(list:list, services:dict) -> str:
    '''
    Print an interpolated string for dictionary value sum

    Keyword arguments:
    list -- a non-empty list
    services -- a non empty dictionary with float or int values

    '''
    # initialize summation variable
    total = 0

    for num in range(0, len(list)):
        if (list[num] == 'No service'):
            continue
        else:
            total += services[list[num]]
    print('Total: $%d' % total)

# Only execute if this is the main script run 
# and script is not imported by another module
if __name__ == "__main__":
    service_menu(services)
    selected_services = service_input(services, 2)
    print('\nDavy\'s auto shop invoice\n')
    service_output(selected_services, services)
    invoice_total(selected_services, services)