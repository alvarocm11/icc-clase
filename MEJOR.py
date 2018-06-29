V_Inicial = float(input("Ingrese la velocidad inicial:"))
Angulo = float(input("Ingrese el angulo al que se va a lanzar el proyectil:"))

theta=Angulo*pi/180
g=9.81

tiempo=(2*V_Inicial*sin(theta))/g

print("Tiempo total de vuelo:", tiempo)
