def mostrar_escenario(escenario):
    print("\t\t\t ESCENARIO\n")
    for fila_escenario in range(0, 50, 10):
        fila = ""
        for columnas_escenario in range(10):
            fila += f"{escenario[fila_escenario + columnas_escenario]}\t"
        print(fila)
    print("\n")
def comprar_entradas(escenario):
    precios = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000,
               6: 100000, 7: 100000, 8: 100000, 9: 100000, 10: 100000,
               11: 100000, 12: 100000, 13: 100000, 14: 100000, 15: 100000,
               16: 100000, 17: 100000, 18: 100000, 19: 100000, 20: 100000,
               21: 50000, 22: 50000, 23: 50000, 24: 50000, 25: 50000,
               26: 50000, 27: 50000, 28: 50000, 29: 50000, 30: 50000,
               31: 10000, 32: 10000, 33: 10000, 34: 10000, 35: 10000,
               36: 10000, 37: 10000, 38: 10000, 39: 10000, 40: 10000,
               41: 10000, 42: 10000, 43: 10000, 44: 10000, 45: 10000,
               46: 10000, 47: 10000, 48: 10000, 49: 10000, 50: 10000}  
    cantidad_entradas = int(input("Ingrese la cantidad de entradas a comprar (1 o 2): "))
    if cantidad_entradas < 1 or cantidad_entradas > 2:
        print("Cantidad inválida.")
        return
    ganancias=0
     
    for elegir_asiento in range(cantidad_entradas):
        mostrar_escenario(escenario)
        asiento = int(input("Seleccione el número del asiento que desea comprar: "))
        if escenario[asiento - 1] == 'X':
            print("El asiento no está disponible.")
            return
        escenario[asiento - 1] = 'X'
        precio = precios[asiento]
        valor_asiento_vendido.append(precio)
        run = input("Ingrese el RUN de la persona que ocupará el asiento (sin puntos, ni digito verificador: ")
        print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {run}.\n")
        if asiento >= 1 and asiento <=20:
            rut_entradas_VIP.append(run)
        elif asiento >= 21 and asiento <=30:
            rut_entradas_normal.append(run)
        elif asiento >= 31 and asiento <=50:
            rut_entradas_economico.append(run)
def ganancias_totales():
    ganancias_entradas = sum(valor_asiento_vendido)
    print('Las ganancias obtenidas con las entradas vendidas son ', ganancias_entradas) 
    volver=input('oprima enter para volver a la opcion principal: ')
    return
def mostrar__rut_compraron_entrada():
    rut_entradas_VIP.sort()
    rut_entradas_economico.sort()
    rut_entradas_normal.sort()
    print(f"Las personas que asistiran a la seccion VIP son ", rut_entradas_VIP,"\nLas personas que asistiran a la seccion normal son ", rut_entradas_normal,"\nLas personas que asistiran a la seccion economica son ", rut_entradas_economico )  
    volver=input('oprima enter para volver a la opcion principal: ')
    return
escenario = []
for puestos in range(1, 51):
    escenario.append(str(puestos))
valor_asiento_vendido = []
rut_entradas_VIP=[]
rut_entradas_normal=[]
rut_entradas_economico=[]
while True:#Menu de venta
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n▌Bienvenido al evento de Michael Jackson▐\n▌\tIngrese opcion\t\t\t▐\n▌\t\t► 1)Comprar entrada\t▐\n▌\t\t► 2)Ver asientos\t▐\n▌\t\t   disponibles\t\t▐\n▌\t\t► 3)Ver listado\t\t▐\n▌\t\t   de asistentes\t▐\n▌\t\t► 4)Mostrar ganancias\t▐\n▌\t\t   totales\t\t▐\n▌\t\t► 5)Salir\t\t▐\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    opciones = int(input("Ingrese opcion: "))
    match opciones:
        case 1:#comprar entrada
            comprar_entradas(escenario)
        case 2:#Ver asientos
            mostrar_escenario(escenario)
        case 3:
            mostrar__rut_compraron_entrada()
        case 4:
            ganancias_totales()
        case 5:
            print('Hasta luego, solo le queda esperar para disfrutar del concierto')
            break
        case _:
            print('Opcion no existe')