temperatura=[]
sumatempertura=0

for n in range (0,23):
    t=int(input("Ingresa la temperatura"))
    temperatura.append(t)
    sumatempertura=+t
print (Temperatura)

promedio=sumatempertura/23

print("El promedio de la temperatura es :", promedio )

if promedio <20:
    print("Revisar la temperatura")
elif 20>= promedio <=30:
    print("La temperatura esta bien")
else:
    print("Revisar la conducta de la temperatura")
