def create_dictionary(*args):
    sorted_dict = {}
    for index, arg in enumerate(args):
        if type(arg) in (dict, list, set):
            print(f"Cannot add {arg} to the dict!")
        else:
            sorted_dict[arg] = index
    return sorted_dict


print(create_dictionary(None, True, 1))

