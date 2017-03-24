l = [1, 2, 30, 4, 5, 65, 7, 4]

# for l in list:
#      if l%2 == 1:
#          print ('previos', l)
#          l = l+1
#          print('new', l)
for i in range (len(l)):
    if l[i] % 2 !=0:
        print('previos', l[i])
        l[i] += 1
        print('new', l[i])
print (l)