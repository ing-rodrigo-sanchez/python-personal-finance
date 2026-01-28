name = input("Ingrese su nombre: ")
print(f"Bienvenido/a {name} a su app de mejora de finanzas personales")

casos = int(input("Ingrese la cantidad de gastos: "))
monto = 0

for _ in range(casos):
    valor = float(input("Ingrese es valor del gasto: $ "))
    monto += valor

print(f"Gastos totales mensuales: ${monto:.2f}")

salario = float(input("Ingrese su salario liquído mensual: $ "))
dinero_total = salario - monto
porcentaje_gastos = (monto / salario) * 100

print(f"Te quedan ${dinero_total:.2f} disponibles")
print(f"El porcentaje de tu sueldo destinado a gastos es de: {porcentaje_gastos:.1f} %")

if porcentaje_gastos <= 50:
    print("😁 Excelente control de gastos")
elif porcentaje_gastos > 50 and porcentaje_gastos <= 80:
    print("🥶 Cuidado, trata de disminuir gastos inecesarios de ser posible")
else:
    print("👹 Cuidado, riesgo financiero alto")

ahorro_recomendado = salario * 0.2
print(f"Ahorro mensual recomendado: 💰$ {ahorro_recomendado:.2f}")
print(f"Monto luego de 1 año: $ {ahorro_recomendado * 12:.2f}")

print(f"Muchas gracias {name} por utilizar la app")
