f1 = open("file4", "r")
f2 = open("file5", "w")

i = 1
for line in f1.readlines():
    print(f2.writelines(str(i) + ': ' + line))
    i += 1

f1.close()
f2.close()

