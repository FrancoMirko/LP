#Input de datos del usuario
edad_autorizada = 18
edad_limite = 17
try:

  edad = int(input("Edad:"))
except ValueError:
  print("Tenes que ingresar un numero valido")
  exit()
if edad >= edad_autorizada:
  print(f"Podes pasar edad autorizada {edad}")
elif edad == edad_limite:
  print(f"Casi casi pa, te falta 1 añito tu edad es {edad}")

else:
 print(f"Sos menor pa, no podes pasar a ningun lado asi")
