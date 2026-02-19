name = input("Ingrese su nombre: ")
print(f"Bienvenido/a {name} a tu app de mejora de finanzas personales")

while True:
    try:
        casos = int(input("Ingrese su numero de gastos: "))
        break
    except ValueError:
        print("Ingrese solo números, refieriendose a su cantidad total de gastos")
monto = 0

for _ in range(casos):
    while True:
        try:
            valor = float(input("Ingrese el valor del gasto: $"))
            break
        except ValueError:
            print("Ingrese solo números, refieriendose al valor de cada gasto")
    monto += valor

print(f"Gastos totales menusales: ${monto:.1f}")

while True:
    try:
        salario = float(input("Ingrese su salario liquido mensual: $"))
        break
    except ValueError:
        print("Ingrese solo números, refiriendose a su salario liquido mensual")

dinero_total = salario - monto
porcentaje_gastos = (monto / salario) * 100

print(f"Luego de pagar los gasos te quedan: ${dinero_total}")
print(f"El porcentaje de tu salario destinado a gastos es de: %{porcentaje_gastos:.1f}")

if porcentaje_gastos <= 50:
    print("😁 Excelente control de gastos")
elif porcentaje_gastos > 50 and porcentaje_gastos <= 80:
    print("🥶 De ser posible, elimina algun gasto innecesario")
else:
    print("👹 Cuidado, riesgo financiero alto")

ahorro_recomendado = salario * 0.2
print(f"Su ahorro recomendado mensual es de: ${ahorro_recomendado:.1f}")
print(f"El monto de su ahorro luego de un año seria de: {ahorro_recomendado * 12:.1f}")

print(f"Muchas gracias {name} por utilizar la app ;)")
