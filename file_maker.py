import sys

def create_file(filename):
    filename= filename.replace(' ', '_')+'.py'
    print(filename)
    f = open(filename, "w")

if len(sys.argv) > 1 and sys.argv[1] != None :
    filename = sys.argv[1]
    create_file(filename)
else:
    filename = input('Enter the name of the file-----')
    create_file(filename)
