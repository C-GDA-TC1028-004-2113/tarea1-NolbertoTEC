def main():
    #escribe tu código abajo de esta línea
    año = float(input("Dame el año de nacimiento: "))
    añoac = float(input("Dame el año actual: "))
    lustros = (añoac-año)/5
    print("Los lustros que has vivido son:",str(lustros))

if __name__ == '__main__':
    main()
