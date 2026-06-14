def filtrar_animais_terrestres(arquivo_entrada):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as file:
            for linha in file:
                linha = linha.strip()

                if not linha:
                    continue

                partes = linha.split(',')

                if len(partes) != 2:
                    continue

                nome = partes[0].strip()
                tipo = partes[1].strip().lower()

                if tipo == "terrestre":
                    print(nome)

    except FileNotFoundError:
        print("Arquivo não encontrado. Sim, isso inclui quando você erra o nome dele.")


arquivo = "animais.txt"
filtrar_animais_terrestres(arquivo)