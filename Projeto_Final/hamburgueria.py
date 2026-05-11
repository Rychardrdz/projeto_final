carrinho = []

while True:
    print("\n=== Hamburgueria ===")
    print("1. Cadastro")
    print("2. Login")
    print("3. Cupom de Desconto")
    print("4. Combos")
    print("5. Bebidas")
    print("6. Carrinho/Finalizar Pedido")
    print("7. Avaliação")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        senha_confirmacao = input("Confirme sua senha: ")

        if senha == senha_confirmacao:
            print(f"Cadastro realizado com sucesso! Bem-vindo, {nome}!")
        else:
            print("Senha incorreta. Por favor, tente novamente.")

    elif escolha == "2":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        print(f"Login realizado com sucesso! Bem-vindo de volta, {nome}!")

    elif escolha == "3":
        print("10% de desconto no seu primeiro pedido!")

    elif escolha == "4":
        print("\nEscolha o tipo de hambúrguer:")
        print("1. X Burguer")
        print("2. X Bacon")
        print("3. X Salada")
        print("4. X Egg")
        print("5. X Tudo")

        hamburguer = input("Digite o número do hambúrguer desejado: ")

        if hamburguer == "1":
            carrinho.append("X Burguer")
            print("Você escolheu um X Burguer.")
        elif hamburguer == "2":
            carrinho.append("X Bacon")
            print("Você escolheu um X Bacon.")
        elif hamburguer == "3":
            carrinho.append("X Salada")
            print("Você escolheu um X Salada.")
        elif hamburguer == "4":
            carrinho.append("X Egg")
            print("Você escolheu um X Egg.")
        elif hamburguer == "5":
            carrinho.append("X Tudo")
            print("Você escolheu um X Tudo.")
        else:
            print("Opção de hambúrguer inválida.")

    elif escolha == "5":
        print("\nEscolha a bebida:")
        print("1. Refrigerante")
        print("2. Suco")
        print("3. Água")

        bebida = input("Digite o número da bebida desejada: ")

        if bebida == "1":
            print("\nOpções de refrigerante:")
            print("1. Coca-Cola")
            print("2. Pepsi")
            print("3. Guaraná")

            refrigerante = input("Digite o número do refrigerante desejado: ")

            if refrigerante == "1":
                print("Você escolheu Coca-Cola.")
            elif refrigerante == "2":
                print("Você escolheu Pepsi.")
            elif refrigerante == "3":
                print("Você escolheu Guaraná.")
            else:
                print("Opção inválida.")

        elif bebida == "2":
            print("\nOpções de suco:")
            print("1. Laranja")
            print("2. Maçã")
            print("3. Uva")

            suco = input("Digite o número do suco desejado: ")

            if suco == "1":
                print("Você escolheu Suco de Laranja.")
            elif suco == "2":
                print("Você escolheu Suco de Maçã.")
            elif suco == "3":
                print("Você escolheu Suco de Uva.")
            else:
                print("Opção inválida.")

        elif bebida == "3":
            print("\nOpções de água:")
            print("1. Água com gás")
            print("2. Água sem gás")

            agua = input("Digite o número da água desejada: ")

            if agua == "1":
                print("Você escolheu Água com gás.")
            elif agua == "2":
                print("Você escolheu Água sem gás.")
            else:
                print("Opção inválida.")

        else:
            print("Opção de bebida inválida.")

    elif escolha == "6":
        print("\n=== CARRINHO / FINALIZAR PEDIDO ===")

    if len(carrinho) == 0:
        print("Seu carrinho está vazio.")

    else:
        for item in carrinho:
            print("-", item)

        finalizar = input("\nDeseja finalizar o pedido? (s/n): ")

        if finalizar == "s":
            print("Pedido finalizado com sucesso!")
            carrinho.clear()

        elif escolha == "7":
            avaliacao = input("Digite sua avaliação de 0 a 5: ")
            print("Obrigado pela sua avaliação!")

        elif escolha == "0":
            print("Obrigado por visitar a Hamburgueria! Até a próxima!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")