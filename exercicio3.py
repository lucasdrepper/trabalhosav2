while True: 
    horas = int(input("Escreva as horas:\n"))
    minutos = int(input("Escreva os minutos:\n"))

    if horas <= 11:
        print(f"São {horas}:{minutos} A.M")
    else:
        print("====================")
        print("    ")
        print(f"São {horas - 12}:{minutos} P.M")
        print("    ")
        print("====================")

    r = int(input("Deseja Continuar?\n 1 - Continuar\n 2 - Sair\n"))

    if r == 1 :
        continue
    if r == 2 :
        print("Finalizando Programa... Até mais!")
        break
