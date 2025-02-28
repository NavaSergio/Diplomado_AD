def factorial(n):
	if n<2:
		return 1
	else:
		return n*factorial(n-1)




# Ejemplo de uso
if __name__ == "__main__":
    numero=input("Ingrese un Numero:")
    x=int(numero)
    y=factorial(x)
    print("El factorial de {} es:{}".format(x,y))
