# Import inflect package to convert numerals into ordinals
# This is used for the service_input function

import inflect
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

def service_input(prompts=2) -> str:
    '''
    TODO: Docstring
    This funciton takes an int num as input and
    iterates num times prompting the user for a desired service.
    Num is converted to its ordinal in the prompt 
    by way of the inflect engine during each iteration
    '''
    # Create an empty list to store loop iteration values
    services_ordered = []
    
    for num in range(1, (prompts + 1)):
        # Uses the ordinal method to convert num to ordinal (e.g. 1 -> 1st)
        # Uses the number_to_words method to convert the ordinal to word (e.g. 1st -> first)
        service_ordered = input('Select %s service: \n' % (ordinal.number_to_words(ordinal.ordinal(num))))
        services_ordered.append(service_ordered)
    print(services_ordered)

# Only execute if this is the main script run 
# and script is not imported by another module

if __name__ == "__main__":
    service_menu(services)
    service_input(2)