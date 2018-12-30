#Numero 1 para el palindromo
numero1 = input("Introduce un numero de tres digitos: \n")

#Numero 2 para el palindromo

numero2 = input("Introduce otro numero de tres digitos: \n")

suma = int(numero1) + int(numero2)

print(suma)

suma_list = []

for i in str(suma):
    suma_list.append(i)

print(suma_list)

cont = 0
cont1 = 0

for i in suma_list:
    cont1 = cont1 +1
    for j in reversed(suma_list):
        if i == j:
                cont = cont + 1

cont = cont / cont1

if cont == len(suma_list):
        print(cont)
        print("Es un palindromo")

else:
        print(cont)
        print("No es un palindromo")
