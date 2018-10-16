#Mostrar por la pantalla la suma de los multiplos de 3 y 5 entre 10
#entre 100 y entre 1000.

print('--------RETO 1-------');

sumMul = 0;

print('Multiplos de 3 y 5 del 1 al 10');

for x in range(1,10):
    if x % 3 == 0 or x % 5 == 0:
        sumMul = sumMul + x;
        print x; #Los imprime dando saltos de linea.

print('Suma de los multiplos de 3 y 5 del 1 al 10'); 
print sumMul;
sumMul = 0; #Reiniciamos el valor del sumatorio de multiplos.

for x in range(1,100):
    if x % 3 == 0 or x % 5 == 0:
        sumMul = sumMul + x;
        print x;

print('Suma de los multiplos de 3 y 5 del 1 al 10');
print sumMul;
sumMul = 0;

for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0:
        sumMul = sumMul + x;
        print x;        
print('Suma de los multiplos de 3 y 5 del 1 al 10');

print sumMul;