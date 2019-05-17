# Import inflect package to convert numerals into ordinals
# This is used for the service_input function
# You must install inflect prior to running
# pip install inflect --user

import inflect

# Create an ordinal variable to convert each service_input loop iteration's 
# int representation into its word representation for readability 
# for the service selection output to the user
ordinal = inflect.engine()

# A dict type is the best data type for services.  
# It yields an associative relationship between service and price.
# It allows for changing prices and adding services, as dicts are mutable.
# Floats are used for the dict values as
# they are the best data type for representing prices
# the dict below uses multiple lines and white space for readability

services = {
    'Oil change': 35.00,
    'Tire rotation': 19.00,
    'Car wash': 7.00,
    'Car wax': 12.00
}

# Loop through the dict of services to output a menu of automotive services
# and the corresponding cost of each service
# A loop is used becasue the dict parameter can be modified
# With dict modification, this loop will not need to change
# and will always reflect the current key:value pairs

def service_menu(services:dict) -> str:
    '''
    Print interpolated strings for key:value pairs.

    Keyword arguments:
    services -- a non-empty dictionary with float or int key values
    '''

    for key, value in services.items():
        print('%s -- $%d' % (key, value))

# Prompt the user for services from the menu
# A loop is used so the code can be easily modified
# To prompt for more or less services as needed in future versions 
# The default is to prompt for input twice

def service_input(services:dict, prompts:int=2) -> list:
    '''
    Return a list of user input elements.

    Keyword arguments:
    services -- a non-empty dictionary
    prompts -- int for number of loop iterations (default 2)

    '''
    # Create an empty list to store loop iteration values
    services_ordered = []
    
    for num in range(1, (prompts + 1)):
        # Uses the ordinal method to convert num to ordinal (e.g. 1 -> 1st)
        # Uses the number_to_words method to convert the ordinal to word (e.g. 1st -> first)
        # The while loop ensures the user enters a valid service from the service menu.
        # Future versions could enhance this validation using case conversion 
        # To render the input-to-dict match case insensitive
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

# Loop thorugh the list of services ordered and output the service and price
def service_output(list:list, services:dict) -> str:
    '''
    Print interpolated strings for list elements

    Keyword arguments:
    list -- a non-empty list
    services -- a non-empty dictionary with float key values

    '''
    for num in range(0, len(list)):
        if (list[num] == 'No service'):
            print('Service %d: No service' % (num + 1))
        else:
            print('Service %d: %s, $%d' % ((num + 1), list[num], services[list[num]]))

# Print the total cost of the services selected
def invoice_total(list:list, services:dict) -> str:
    '''
    Print an interpolated string for dictionary value sum

    Keyword arguments:
    list -- a non-empty list
    services -- a non empty dictionary with float key values

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