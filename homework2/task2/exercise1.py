s = """We are not what we should be! We are not what we need to be. But at least we are not what we used to be"""

s1 = s.split(' ')
print(s1)

# кол-во слов в тексте
print("Amount of words: ", len(s1))

#print(type(s1))

# Удаление знаков препинания
s2 = ""
for elem in s:
    if elem not in ("!", "."):
        s2 = s2 + elem
print(s2)

# слова в алфавитном порядке
s3 = s1.sort()
print(s1)

