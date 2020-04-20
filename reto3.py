#Crear un programa que diga si un numero es primo o no.

print("Introduce un numero")
num=input()

num2 = 2

comprobacion = 0
contador = 0
y = num

for x in range(1,num):
    y -=1
    if num % num2 == 0:
        if contador != 0:
            comprobacion = 1
            contador += 1
            break

        else:
            if contador == 0:
                if y == 1:
                    comprobacion = 0
                    break

                else:
                    comprobacion = 1
                    break

            else:
                comprobacion = 1
                break

    else:
        if num == num2: 
            if contador == 0:
                comprobacion = 0
        
        else:
            num2 += 1


if comprobacion == 0:
    print("Es primo")
else:
    print("No es primo")