def perguntar_turno():
    while True:
        turno = input("Olá, em qual turno você estuda? (manhã, tarde ou noite): ").strip().lower()

        if turno in ["manhã", "manha"]:
            print("Bom dia!")
            break
        elif turno == "tarde":
            print("Boa tarde!")
            break
        elif turno == "noite":
            print("Boa noite!")
            break
        else:
            print("Turno inválido, tente novamente.")