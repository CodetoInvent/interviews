def split_options_string(options_string=''):
    """
    The options string is formatted as device1dimension1=value1,
    device1dimension2=value2&device2dimension1=value3 so we first split on
    ampersands and then split again on commas to get all the keys/values for our
    dictionaries.
    """
    options_string = options_string.strip()
    if options_string == 'none' or not options_string:
        return []

    models = options_string.split('&')

    devices = [] 
    for model in models:
        mapping = {}
        for attributes in model.split(','):
            attribute = attributes.split('=')
            if len(attribute) != 2: 
                raise ValueError('Invalid attribute set') 

            k, v = attribute
            mapping[k] = v

        devices.append(mapping)

    return devices

print split_options_string('model=sailfish&version=22,model=Nexus5')
