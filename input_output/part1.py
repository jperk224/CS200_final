# A dict type is the best data type for services.  
# It allows for an associative relationship between and service and price.
# It allows for changing prices and adding services, as dicts are mutable.
# Floats are use, as they are the best data type for representing prices

services = {
    'Oil change': 35.00,
    'Tire rotation': 19.00,
    'Car wash': 7.00,
    'Car wax': 12.00
}

# print(services)

def service_menu(services):
    '''
    TODO: Enter Docstring
    '''
    for item in services:
        print(item)

service_menu(services);