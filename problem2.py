#Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#By starting with 1 and 2, the first 10 terms will be:
#
#       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

total = int(input("Introduce el numero de terminos de fibonacci: "))
anterior = 0
actual = 1
suma = 0

for x in range (0,total):
    print(x)
    aux = actual
    actual += anterior
    anterior = aux
    if actual % 2 == 0:
        suma += actual
        valor = str(suma)
        print("la suma es:" + valor)
        print(actual)
