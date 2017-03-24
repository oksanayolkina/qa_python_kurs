def distance(x1, y1, x2, y2):
    result = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return result

if __name__ == "__main__":
    x1 = int(input("Input x1: "))
    y1 = int(input("Input y1: "))
    x2 = int(input("Input x2: "))
    y2 = int(input("Input y2: "))
    print("Distance = ", distance(x1, y1, x2, y2))