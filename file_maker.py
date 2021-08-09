import sys

def create_file(filename):
    filename= filename.replace(' ', '_')+'.py'
    print(filename)
    f = open(filename, "w")

if len(sys.argv) > 1 and sys.argv[1] != None :
    list_name = sys.argv[1:]
    filename = '_'.join(list_name)

    create_file(filename)
else:
    filename = input('Enter the name of the file-----')
    create_file(filename)
