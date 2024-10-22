def pode_entrar_na_balada():
    print("bem-vindo à balda do dudu!")
    idade = int(input("informe sua idade: "))

    if idade >= 18:
        print("pode entrar! :)")
    elif idade>= 16:
        autorizacao = input("você tem autorização dos pais? (sim/não): ").strip().lower()
        if autorizacao == "sim":
            print("pode entrar! :)")
        else:
            print("não pode entrar! :( ")
    else:
        print("não pode entrar! :( ")

pode_entrar_na_balada()