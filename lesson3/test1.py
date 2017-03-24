def word_printer (word, count=1, wow=0):
    if wow == 1:
        print((word * count).upper())
    else:
        print(word * count)
word_printer("Asd", 3, count=5)
