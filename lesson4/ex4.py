f1 = open("file", "r")
f2 = open("file1.txt", "w")

all = f1.read()

lines = all.split("\n")

i = 0
for line in lines:
    f2.write(str(i) + ': ' + line + "\n")
    i += 1
    print(i)
