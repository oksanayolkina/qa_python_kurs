from homework3.class_Worker import Worker

a = Worker('Ivanov Ivan', "qa team lead", 10000, 10)
b = Worker('Semenov Semen', 'qa automation', 3000, 5)
c = Worker('Petrov Petro', 'qa automation', 2000, 2)
d = Worker('Vasachkin Vasya')


print(d.get_salary(2))
