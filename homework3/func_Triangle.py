def triangle(a, b, c):
   if (a + b > c) and (b + c > a) and (a + c > b):
       return True
   else:
       return False


if __name__ == "__main__":

    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    print(triangle(a, b, c))



