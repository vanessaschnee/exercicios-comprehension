dobros_pares = []

for i in range(10):
    if i % 2 == 0:
        i = i * 2
        dobros_pares.append(i)

print(dobros_pares)

#Comprehension
##[Expressão da lista, for item in lista, if condicional]

dobros_pares_comprehension = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_pares_comprehension)