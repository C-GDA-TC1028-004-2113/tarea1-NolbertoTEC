def main():
    #escribe tu código abajo de esta línea
    mens = int(input("Dame el número de mensajes: "))
    megs = float(input("Dame el número de megas: "))
    mins = int(input("Dame el número de minutos: "))
    costo = (mens*0.80)+(megs*0.80)+(mins*0.80)
    print("El costo mensual es:", str(costo))

if __name__ == '__main__':
    main()
