#Generator -consumo sob demanda-
##(Expressão, for item in lista, if condicional)

generator = ( i * 2 for i in range(5) if i % 2 == 0)

for numero in generator:
    print(numero)


