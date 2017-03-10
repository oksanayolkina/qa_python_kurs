s = input("Enter words or numbers: ")

s1 = s.isalpha()
s2 = s.isdigit()

if s1 == True:
     print ("Result: letters")
elif s2 == True:
     print ("Result: numbers")
else:
     print ("Result: letters & numbers")

print ("Number of characters: ", len(s))