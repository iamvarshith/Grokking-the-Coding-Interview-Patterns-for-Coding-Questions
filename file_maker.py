import sys


def create_file(filename1,path1 = None):
    filename1 = filename1.replace(' ', '_') + '.py'
    final = path1 + '\\'+ filename1
    print('final '+ final)
    f = open(final, "w")


if len(sys.argv) > 1 and sys.argv[1] != None:
    list_name = sys.argv[2:]

    path1 = sys.path[0] + '\\' + sys.argv[1]
    filename1 = '_'.join(list_name)
    print(sys.path[0])

    create_file(filename1,path1)
else:
    filename1 = input('Enter the name of the file-----')
    create_file(filename1)
