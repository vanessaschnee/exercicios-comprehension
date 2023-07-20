dobros = []

for i in range(10):
    i = i * 2
    dobros.append(i)

print(dobros)

#Comprehension
##[Expressão da lista, for item in lista]

dobros_comprehension = [i * 2 for i in range(10)]
print(dobros_comprehension)