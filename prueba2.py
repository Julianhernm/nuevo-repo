

def imprimir_partida(partida, ultimo):
    print("+----------------------+------------+------------+")
    print("| Cuenta               |   Debe     |   Haber    |")
    print("+----------------------+------------+------------+")
    for cuenta, debe, haber in partida:
        print(f"| {cuenta.ljust(20)} | {str(debe).rjust(10)} | {str(haber).rjust(10)} |")
        if haber == ultimo:
            print("+----------------------+------------+------------+")
    print("+----------------------+------------+------------+")


# Ingreso de operarios y trabajo hecho
operarios = {}
num_operarios = int(input("Ingrese la cantidad de operarios: "))

for _ in range(num_operarios):
    nombre = input("Ingrese el nombre del operario: ")
    operarios[nombre] = {"lunes": 0, "martes": 0, "miercoles": 0, "jueves": 0, "viernes": 0, "sabado": 0,
                         "horas_extras": 0}
    for dia in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]:
        operarios[nombre][dia] = int(input(f"Ingrese la cantidad de prendas hechas el {dia} por {nombre}: "))
    operarios[nombre]["horas_extras"] = int(input(f"Ingrese la cantidad de horas extras trabajadas por {nombre}: "))
    operarios[nombre]["judicial"] = int(input("ingrese la cantidad judicial: "))
    operarios[nombre]["anticipos"] = int(input("ingrese los anticipos: "))

def imprimir_tabla(operarios):
    total_MD = 0
    total_bonificacion = 0
    total_igss = 0
    total_devengados = 0
    total_judicial = 0
    total_anticipos = 0
    total_descuentos_colum = 0
    total_salario_liquido = 0

    print(
        "+----------------------+----------------+--------+--------+--------+--------+--------+--------+-----------+--------------+----------------+----------+-----------+--------------+-----------------+---------+-----+----------+-----------+----------+--------------+-")
    print(
        "| Nombre               | Días Laborados |   L    |   M    |   M    |   J    |   V    |   S    | Ordinario | horas extras | Extraordinario | 7mo Día  | Subtotal  | Bonificación | Total Devengado |   IGSS  | ISR | Judicial | Anticipos | Total D. | Salario liq. |")
    print(
        "+----------------------+----------------+--------+--------+--------+--------+--------+--------+-----------+--------------+----------------+----------+-----------+--------------+-----------------+---------+-----+----------+-----------+----------+--------------+-")
    for nombre, trabajo in operarios.items():
        dias_laborados = sum(1 for prendas in trabajo.values() if isinstance(prendas, int) and prendas > 0)-1
        total_prendas = sum(trabajo[dia] for dia in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"])
        ordinario = total_prendas
        extraordinario = ((ordinario / dias_laborados) / 8) * 1.5 * trabajo["horas_extras"] if dias_laborados > 0 else 0
        septimo_dia = (ordinario + extraordinario) / 6 if dias_laborados == 6 else 0
        subtotal = ordinario + extraordinario + septimo_dia
        bonificacion = (250 / 31) * (7 if dias_laborados == 6 else (5 if dias_laborados == 5 else 7 - (6 - dias_laborados) - 1))
        total_devengado = subtotal + bonificacion
        iggs = round(subtotal * 0.0483, 2)
        total_descuentos = iggs + trabajo["judicial"] + trabajo["anticipos"]
        salario_liquido = total_devengado - total_descuentos
        total_MD = total_MD + subtotal
        total_bonificacion = total_bonificacion + bonificacion
        total_igss = total_igss + iggs
        total_devengados = total_devengados + total_devengado
        total_judicial += trabajo["judicial"]
        total_anticipos += trabajo["anticipos"]
        total_salario_liquido += salario_liquido
        total_descuentos_colum += total_descuentos

        print(f"| {nombre.ljust(20)} | {str(dias_laborados).rjust(14)} | {str(trabajo['lunes']).rjust(6)} | {str(trabajo['martes']).rjust(6)} | {str(trabajo['miercoles']).rjust(6)} | {str(trabajo['jueves']).rjust(6)} | {str(trabajo['viernes']).rjust(6)} | {str(trabajo['sabado']).rjust(6)} | {str(ordinario).rjust(9)} | {str(round(trabajo["horas_extras"], 2)).rjust(12)} | "f"{str(round(extraordinario, 2)).rjust(14)} | {str(round(septimo_dia, 2)).rjust(8)} | {str(round(subtotal, 2)).rjust(9)} | {str(round(bonificacion, 2)).rjust(12)} | {str(round(total_devengado, 2)).rjust(15)} | {str(round(iggs, 2)).rjust(7)} | {str(round(0, 2)).rjust(3)} | {str(round(trabajo["judicial"], 2)).rjust(8)} | {str(round(trabajo["anticipos"], 2)).rjust(9)} | {str(round(total_descuentos, 2)).rjust(8)} | {str(round(salario_liquido, 2)).rjust(12)} |")
    cuotas_patronales = round(total_MD * 0.1267, 2)
    igss_por_pagar = cuotas_patronales + total_igss
    print(f"| {"TOTAL".ljust(20)} | {str(0).rjust(14)} | {str(0).rjust(6)} | {str(0).rjust(6)} | {str(0).rjust(6)} | {str(0).rjust(6)} | {str(0).rjust(6)} | {str(0).rjust(6)} | {str(0).rjust(9)} | {str(0).rjust(12)} | "f"{str(0).rjust(14)} | {str(0).rjust(8)} | {str(round(total_MD, 2)).rjust(9)} | {str(round(total_bonificacion, 2)).rjust(12)} | {str(round(total_devengados, 2)).rjust(15)} | {str(round(total_igss, 2)).rjust(7)} | {str(0).rjust(3)} | {str(round(total_judicial, 2)).rjust(8)} | {str(round(total_anticipos, 2)).rjust(9)} | {str(round(total_descuentos_colum, 2)).rjust(8)} | {str(round(total_salario_liquido, 2)).rjust(12)} |")
    print(
        "+----------------------+----------------+--------+--------+--------+--------+--------+--------+-----------+--------------+----------------+----------+-----------+--------------+-----------------+---------+-----+----------+-----------+----------+--------------+-")
    print("")
    print("")
    partida_ejemplo = [
        ("mano de obra directa", round(total_MD, 2), ""),
        ("cuotas patronales", cuotas_patronales, ""),
        ("bonificacion inc.", round(total_bonificacion, 2), ""),
        ("  a:bancos", "", round(total_salario_liquido, 2)),
        ("    igss por pagar", "", igss_por_pagar),
        ("TOTAL", round((total_MD+cuotas_patronales+total_bonificacion), 2), round((total_salario_liquido+igss_por_pagar), 2))
    ]

    imprimir_partida(partida_ejemplo, igss_por_pagar)


imprimir_tabla(operarios)


