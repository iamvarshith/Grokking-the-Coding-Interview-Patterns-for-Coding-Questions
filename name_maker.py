def create_file(filename):
    filename= filename.replace(' ', '_')+'.py'
    print(filename)
    f = open(filename, "w")


filename = input('Enter the name of the file')
create_file(filename)
