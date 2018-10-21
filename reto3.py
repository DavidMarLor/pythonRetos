#Crear un programa que diga si un numero es primo o no.

print("Introduce un numero");
num=input();

num2 = 2;

#def primo(num, num2):
#    if num % num2 == 0:
#        return 1;
#    else:
#        num2 += 1;
#        auxiliar = primo(num, num2);
#        return auxiliar;

comprobacion = 0;
contador = 0;

#Se debe comrpobar hasta que num y num2 sean iguales
#Se puede intentar con un for.

for x in range(0,num):
    if num % num2 == 0:
        print("He entrado en el if");
        if contador != 0:
            comprobacion = 1;
            contador += 1;
            print("He entrado en el if del if");
        else:
            comprobacion = 0;
            print("He entrado en el else del if");

    elif num == num2:
        if contador == 0:
            comprobacion = 0;
        print("He entrado en el elif");

    else:
        num2 += 1;
        print num2;
        print("He entrado en el else");


#comprobacion = primo(num,num2);

if comprobacion == 0:
    print("Es primo");
else:
    print("No es primo");