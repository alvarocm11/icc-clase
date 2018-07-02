V_Inicial = float(input("Ingrese la velocidad inicial:"))
Angulo = float(input("Ingrese el angulo al que se va a lanzar el proyectil:"))

theta=Angulo*pi/180
g=9.81

tiempo=(2*V_Inicial*sin(theta))/g
alturamax=((V_Inicial**2)*(sin(theta)**2))/2*g
distance=(V_inicial*cos(theta))*time

print("Tiempo total de vuelo:", tiempo,"s")
print("La altura maxima es:",alturamax,"m")
print("La distancia recorrida total es:",distance,"m")
