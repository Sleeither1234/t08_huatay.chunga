#asignacion de un valor de una varaible en la cual haremos 15 ejercicios
#      012345678912345678912345678912345678912345678912345678912345678
frase="CUANDO APRENDAS A ESTAR SOLO DISFRUTARAS LA COMPAÑIA DE OTRO..."
#(-1)  987654321987654321987654321987654321987654321987654321987654321
print(len(frase))
#ejercicio 01
print(frase[0:5])       #impresion de cuando

#ejercicio 02
print(frase[5::-1])     #impresion de cuando al reves

#ejercicio 03
print(frase[7:28])      #impresion de la palabra APRENDAS A ESTAR SOLO

#ejercicio 04
print(frase[-56:-35])     #impresion de la misma palabra del anterior ejemplo pero escrita con indexacion de numeros negativos

#ejercicio 05
print(frase[50:43:-1])           #se imprime la palabra compañia al reves

#ejercicio 06
print(frase[::-1])              #se imprime la variable frase al reves

#ejercicio 07
print(frase[59:54:-1])           #se imprime la palabra otro al reves

#ejercicio 08
print(frase[:8:-1])        #se imprime desde la indexacion 8 hacia delante pero al reves

#ejercicio 09
print(frase[-4:-13:-1])    #se imprime desde la indexacion -4 hasta el -13 pero al reves

#ejercicio 10
print(frase[24:28]+"\n"+frase[-4:-9:-1]) #se concatena dos cortados de cadenas de la variable frase

#ejercicio 11
print("el codigo es: "+frase[22:17:-1]) #se imprime una cadena y un cortado de cadena de la variable frase

#ejercicio 12
print("mi nombre es\t"+frase[-23:-28:-1]) #se imprime unas cadenas y cortado con el nombre sara de la variable frase

#ejercicio 13
print(frase[-22:-11]+" de "+frase[-23:-28:-1]+" es muy exitosa")

#ejercicio 14
print("ES MEJOR QUE "+frase[7:28])  #se imprime la union de una cadena y un cortado de cadena

#ejercicio 15
print(frase[24:40]+" el baile")