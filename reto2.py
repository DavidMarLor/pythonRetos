#Sacar la suma de los valores pares de la serie de fibonacci para una serie de elementos.

print("Introduce un numero de elementos para la serie de Fibonacci");
numElem = input();


print('Ha introducido: ', numElem);

auxiliar = 1;
auxiliar2 = 1;
total = 0;

print auxiliar;
print auxiliar2;

for x in range(0 , numElem):
    
    cont = auxiliar + auxiliar2;
    print cont;

    if cont % 2 == 0: 
        total = cont + total;

    #Intercambio de valores para realizar fibonacci
    auxiliar2, auxiliar = auxiliar, auxiliar2;
    auxiliar, cont = cont, auxiliar;


print("El total de los pares es: ");
print total;

