class empleado:
    def calcular_salario(self):
        pass  


class empleadoporHora(empleado):
    def __init__(self, horas_trabajadas, pago_por_hora):
        self.horas = horas_trabajadas
        self.pago = pago_por_hora

    def calcular_salario(self):
        return self.horas * self.pago


class empleadoFijo(empleado):
    def __init__(self, salario_mensual):
        self.salario = salario_mensual

    def calcular_salario(self):
        return self.salario


if __name__ == "__main__":
    empleados = [
        empleadoporHora(35, 1430),
        empleadoFijo(20000),
        empleadoporHora(15, 1200),
        empleadoFijo(84500)
    ]

    total = 0
    for e in empleados:
        salario = e.calcular_salario()
        print(f"Salario: ${salario}")
        total += salario

    print(f"\nSalario total a pagar: ${total}")