def is_valid_name(name):
    valid_characters = "_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in name:
        if not i in valid_characters:
            return False

    '''numbers = "0123456789"
    if name[0] in numbers:
        return False'''

    return True

def is_valid_name_2(name):
    for i in name:
        if not (i.isalnum() or i == "_"):
            return False
    '''return name[0] not in "0123456789"'''

def fix_name(boolean, name):
    while boolean == True:
        if name[0] in "0123456789":
            a = list(name)
            a[0] = "_"
            new_name = "".join(a)
            return new_name
        else:
            print("It doesn't need to be fixed.")
            return name


name = "_3aosd_1sad"
print(fix_name(is_valid_name(name), name))
