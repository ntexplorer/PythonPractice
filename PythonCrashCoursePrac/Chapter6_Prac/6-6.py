favorite_languages = {
    'jen': "python",
    'sarah': "c",
    'edward': 'ruby',
    'phil': 'python'}
name_list = ['sarah', 'tom', 'lisa', 'edward']
for name in name_list:
    if name in favorite_languages.keys():
        print("{}, thank you for taking the investigation.".format(name.title()))
    else:
        print("{}, would you like to take an investigation?".format(name.title()))
