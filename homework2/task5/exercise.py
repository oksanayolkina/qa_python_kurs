a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

def triangle (a, b, c):
   if (a + b > c) and (b + c > a) and (a + c > b):
       return True
   else:
       return False
print(triangle(a, b, c))



