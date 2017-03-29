f1 = open("file", "r")
f2 = open("file3.txt", "w")

lines = f1.readlines()

i = 0
# for line in lines: или
for line in f1:
    f2.write(str(i) + ': ' + line)
    i += 1

f1.close()
f2.close()
