# Import inflect package to convert numerals into ordinals
# This is used for the service_input function
# You must install inflect prior to running
# pip install inflect --user

import inflect

# Create an ordinal variable to convert each service_input loop iteration's 
# int representation into its word representation 
# for the service selection output to the user
ordinal = inflect.engine()

# A dict type is the best data type for services.  
# It yields an associative relationship between service and price.
# It allows for changing prices and adding services, as dicts are mutable.
# Floats are used for the dict values
# they are the best data type for representing prices

services = {
    'Oil change': 35.00,
    'Tire rotation': 19.00,
    'Car wash': 7.00,
    'Car wax': 12.00,
}


# Loop through the dict of services to output a menu of automotive services
# and the corresponding cost of each service
# The dict can be modified, this loop will not need to change
# and will always reflects the current dict

def service_menu(dict:services) -> str:
    '''
    TODO: Shore this up
    This function takes a dictionary as input and 
    returns a string for each key:value pair.
    The key and value are interpolated into the string output.
    '''
    for key, value in services.items():
        print('%s -- $%d' % (key, value))

# Prompt the user for two services from the menu
# A loop is used so the code can be easily modified
# To prompt for more or less services as needed 

def service_input(dict:services, prompts=2) -> list:
    '''
    TODO: Docstring
    This function takes an int num as input and
    iterates num times prompting the user for a desired service.
    Num is converted to its ordinal in the prompt 
    by way of the inflect engine during each iteration
    '''
    # Create an empty list to store loop iteration values
    services_ordered = []
    
    for num in range(1, (prompts + 1)):
        # Uses the ordinal method to convert num to ordinal (e.g. 1 -> 1st)
        # Uses the number_to_words method to convert the ordinal to word (e.g. 1st -> first)
        # The while loop ensures the user enters a valid service from the services dict
        # Future versions could enhance this funciton using case conversion 
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

def service_output(list, dict:services) -> str:
    '''
    TODO: Docstring
    '''
    for num in range(0, len(list)):
        if (list[num] == 'No service'):
            print('Service %d: No service' % (num + 1))
        else:
            print('Service %d: %s, $%d' % ((num + 1), list[num], services[list[num]]))

# Print the total cost of the services selected

def invoice_total(list, dict:services) -> str:
    '''
    TODO: Docstring
    '''
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
    print('Davy\'s auto shop invoice\n')
    service_output(selected_services, services)
    invoice_total(selected_services, services)