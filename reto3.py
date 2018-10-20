#Crear un programa que diga si un numero es primo o no.

print("Introduce un numero");
num=input();

num2 = 2;

def primo(num, num2):
    if num % num2 == 0:
        return 1;
    else:
        num2 += 1;        
        return 0;         

comprobacion = primo(num,num2);

if comprobacion == 0:
    print("Es 1");
else:
    print("Es un 0");