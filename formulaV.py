
#Escribimos una funcion
def formula (num1, num2):
    velocidad=num1/num2
    print(num1,"m/",num2,"s =",velocidad,"m/s")
    return velocidad

#pedimos los datos al usuario para encontrar la velocidad
num1=int(input("Ingrese la distancia recorrida en metros: "))
num2=int(input("Ingrese el lapso de tiempo en segundos: "))
#llamamos a la función
formula(num1,num2)