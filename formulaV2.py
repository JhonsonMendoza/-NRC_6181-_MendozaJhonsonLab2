#Escribimos una funcion
def formula (num1, num2):
    #funcionalidad: obtener una velocidad de acuerdo a los datos ingresados
    velocidad=num1/num2
    print(num1,"Km/",num2,"h =",velocidad,"Km/h")
    #mostrar la formula usada y que unidades de medida usa.
    return velocidad

#pedimos los datos al usuario para encontrar la velocidad
num1=int(input("Ingrese la distancia recorrida en Kilometros: "))
num2=int(input("Ingrese el lapso de tiempo en horas: "))
#llamamos a la función
formula(num1,num2)