#Ingreso de datos para realizar calculos matematicos con validación para que solo sean numeros
while True:
  try:
    num_1 = float(input("Ingrese el primer digito:"))
    num_2 = float(input("Ingrese el segundo digito:"))
    oa = input("ingrese la operacion aritmetica ").strip()

    if oa.lower() == "q":
        print("Saliendo de la calculadora")
        break
  except ValueError:
    print("Ingresa un numero alfanumerico!")
    continue ##Volver a pedir datos##

#Operaciones aritmeticas
    #Multiplicacion
  if oa == "*":
    resultado = num_1 * num_2
    print(f"El Resultado es:{resultado}") 

    #Suma
  elif oa == "+":
    resultado = num_1 + num_2
    print(f"El resultado es: {resultado}")

    #Resta
  elif oa == "-":
    resultado = num_1 - num_2
    print(f"El resultado es: {resultado}")    
    
    #Division
  elif oa == "/":
    if num_2 == 0:
        print("No se puede dividir por 0")
    continue
    resultado = num_1 / num_2
    print(f"El resultado es: {resultado}")

  else:
    print("Operacion no soportada. Usa + ,- ,* o /")
    continue

