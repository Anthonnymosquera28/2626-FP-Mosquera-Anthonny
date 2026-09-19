#calcular el area de un rectangulo
def calcular_area_rectangulo(base, altura):
     area = base * altura
     return area

print("---SISTEMA DE CALCULO DEL ÁREA DE UN RECTANGULO---")
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

print("-------------------------------------------------")
resultado =calcular_area_rectangulo (base, altura)

print(f"El área del rectangulo es {resultado}")