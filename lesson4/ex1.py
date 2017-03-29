my_file = open("files", "r")
my_file.read()

my_file1 = open("files", "w")
my_file1.write("Hello, python!")
my_file1.close()

my_file2 = open("files", "a")
my_file2.write(" Hello, world!")
my_file2.close()
my_file2 = open("files", "r")
qw = my_file2.read()

print(qw)
