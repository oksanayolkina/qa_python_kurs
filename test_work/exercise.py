from test_work.classTest import Worker

a = Worker("Ivan Ivanov", "qa team lead", 10000, 10)
#b = Worker('Semenov Semen', 'qa automation', 3000, 20)
#c = Worker('Petrov Petro', 'qa automation', 2000, 30)
#d = Worker('Vasachkin Vasya')

a.__full_name = '1111 111'

a.set_lastname('Vasilenko')
a.set_firstname('Vasya')

print(a.get_firstname())
print(a.get_lastname())



