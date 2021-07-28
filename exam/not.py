import os
filename = input('Enter the file name: ')
if not os.path.isfile(filename):
    print('ERROR: File does not exist!')
else:
    print('The file is there.')
# IDE - integrated development environment
