#Input de datos del user
nombre =input("Nombre del usuario:")

#Validacion del saldo
try:
  saldo_actual = float(input("Ingresa tu saldo actual:"))
except ValueError:
    print("Ingresa un monto valido!")

#Validacion del costo
try:      
  costo = float(input("Costo del viaje:"))
except ValueError:
    print("Ingresa un numero valido!")
    exit()
if costo > saldo_actual:
  print("Saldo insuficiente")

else:
  saldo_restante = saldo_actual-costo
  print(f"Buen viaje! {nombre}, tu saldo restante es:${saldo_restante:.2f}")