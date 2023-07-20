#Generator -consumo sob demanda, menor demanda de memória-
##(Expressão, for item in lista, if condicional)

generator = ( i * 2 for i in range(5) if i % 2 == 0)
print(next(generator)) # Saída 0
print(next(generator)) # Saída 2
print(next(generator)) # Saída 4
# print(next(generator)) # Erro!


