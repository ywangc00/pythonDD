#Pedir al usuario 3 números reales (x, y, z ) y que muestre en pantalla el resultado de x^2 + y - z.

print( "Creado por Daniela Valentina De Nóbrega. " )

#Introduzca los 3 números:
x,y,z = (1.2323, 2.53232, 3.1232)

#Redondeamos el resultado a solo 3 decimales con round ()
resultado = round (x*x + y - z , 3)

print(  "El resultado es " , resultado )