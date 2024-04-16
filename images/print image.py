import os
content = os.listdir('.')
for file_name in content:
    if 'LINE' in file_name:
        print ("<img src=\"images\\{0}\" alt=\"{1}\">".format(file_name, file_name[0:-4]))