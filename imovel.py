import csv

def calcular_aluguel(tipo, quartos, garagem, criancas, vagas_extra=0):
    """
    Calcula o valor mensal do aluguel com base no tipo de imóvel, número de quartos, garagem e outras opções.
    """
    # Valores base
    precos = {
        "apartamento": 700.00,
        "casa": 900.00,
        "estudio": 1200.00
    }
    aluguel = precos[tipo]

    # Acréscimos de quartos
    if tipo == "apartamento" and quartos == 2:
        aluguel += 200.00
    elif tipo == "casa" and quartos == 2:
        aluguel += 250.00

    # Garagem / estacionamento
    if tipo in ["apartamento", "casa"] and garagem:
        aluguel += 300.00
    elif tipo == "estudio":
        # Estúdio: 2 vagas = +250, vagas extras = +60 cada
        aluguel += 250.00
        if vagas_extra > 0:
            aluguel += vagas_extra * 60.00

    # Desconto de 5% para apartamentos sem crianças
    if tipo == "apartamento" and not criancas:
        aluguel *= 0.95

    return aluguel


def gerar_parcelas_csv(nome_cliente, aluguel, contrato_total=2000.00, parcelas_contrato=5):
    """
    Gera um arquivo CSV com as 12 parcelas mensais do aluguel e parcelas do contrato.
    """
    valor_contrato_parcela = contrato_total / parcelas_contrato
    total_mensal = aluguel + valor_contrato_parcela

    with open(f"orcamento_{nome_cliente}.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Mês", "Aluguel (R$)", "Contrato (R$)", "Total Mensal (R$)"])
        
        for mes in range(1, 13):
            if mes <= parcelas_contrato:
                total = aluguel + valor_contrato_parcela
                writer.writerow([mes, f"{aluguel:.2f}", f"{valor_contrato_parcela:.2f}", f"{total:.2f}"])
            else:
                writer.writerow([mes, f"{aluguel:.2f}", "0.00", f"{aluguel:.2f}"])
    
    print(f"\n📂 Arquivo gerado com sucesso: orcamento_{nome_cliente}.csv")


def main():
    print("=== 🏘️ SISTEMA DE ORÇAMENTO - R.M IMOBILIÁRIA ===\n")
    nome = input("Nome do cliente: ").strip().replace(" ", "_").lower()

    print("\nTipos de imóvel disponíveis:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    tipo_opcao = input("Escolha o tipo (1/2/3): ")

    if tipo_opcao == "1":
        tipo = "apartamento"
    elif tipo_opcao == "2":
        tipo = "casa"
    elif tipo_opcao == "3":
        tipo = "estudio"
    else:
        print("Opção inválida.")
        return

    quartos = 1
    if tipo in ["apartamento", "casa"]:
        qtd_quartos = input("Deseja 2 quartos? (s/n): ").lower()
        if qtd_quartos == "s":
            quartos = 2

    garagem = False
    vagas_extra = 0

    if tipo in ["apartamento", "casa"]:
        g = input("Deseja incluir garagem? (s/n): ").lower()
        if g == "s":
            garagem = True
    elif tipo == "estudio":
        e = input("Deseja incluir estacionamento (2 vagas + R$250)? (s/n): ").lower()
        if e == "s":
            vagas_extra = int(input("Quantas vagas extras deseja além das 2 inclusas? (0 = nenhuma): "))

    criancas = input("O cliente possui crianças? (s/n): ").lower() == "s"

    aluguel = calcular_aluguel(tipo, quartos, garagem, criancas, vagas_extra)

    print("\n=== RESUMO DO ORÇAMENTO ===")
    print(f"Tipo de imóvel: {tipo.capitalize()}")
    print(f"Quartos: {quartos}")
    if tipo in ["apartamento", "casa"]:
        print(f"Garagem: {'Sim' if garagem else 'Não'}")
    elif tipo == "estudio":
        print(f"Vagas de estacionamento extras: {vagas_extra}")
    print(f"Crianças: {'Sim' if criancas else 'Não'}")
    print(f"Valor mensal do aluguel: R$ {aluguel:.2f}")
    print("Contrato imobiliário: R$ 2.000,00 (até 5x)")
    print(f"Total mensal (com contrato parcelado): R$ {aluguel + 2000/5:.2f}")

    gerar_parcelas_csv(nome, aluguel)


if __name__ == "__main__":
    main()



import csv


def calcular_aluguel(tipo, quartos, garagem, criancas, vagas_extra=0):


    precos = {
        "apartamento": 700.00,
        "casa": 900.00,
        "estudio": 1200.00
    }
    aluguel = precos[tipo]


    if tipo == "apartamento" and quartos == 2:
        aluguel += 200.00
    elif tipo == "casa" and quartos == 2:
        aluguel += 250.00




    if tipo in ["apartamento", "casa"] and garagem:
        aluguel += 300.00
    elif tipo == "estudio":
        aluguel += 250.00
        if vagas_extra > 0:
            aluguel += vagas_extra * 60.00


    if tipo == "apartamento" and not criancas:
        aluguel *= 0.95


    return aluguel




def gerar_parcelas_csv(nome_cliente, aluguel, contrato_total=2000.00, parcelas_contrato=5):
   
    valor_contrato_parcela = contrato_total / parcelas_contrato
    total_mensal = aluguel + valor_contrato_parcela


    with open(f"orcamento_{nome_cliente}.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Mês", "Aluguel (R$)", "Contrato (R$)", "Total Mensal (R$)"])
       
        for mes in range(1, 13):
            if mes <= parcelas_contrato:
                total = aluguel + valor_contrato_parcela
                writer.writerow([mes, f"{aluguel:.2f}", f"{valor_contrato_parcela:.2f}", f"{total:.2f}"])
            else:
                writer.writerow([mes, f"{aluguel:.2f}", "0.00", f"{aluguel:.2f}"])
   
    print(f"\n📂 Arquivo gerado com sucesso: orcamento_{nome_cliente}.csv")




def main():
    print("SISTEMA DE ORÇAMENTO - R.M IMOBILIÁRIA\n")
    nome = input("Nome do cliente: ").strip().replace(" ", "_").lower()


    print("\nTipos de imóvel disponíveis:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")


    tipo_opcao = input("Escolha o tipo (1/2/3): ")


    if tipo_opcao == "1":
        tipo = "apartamento"
    elif tipo_opcao == "2":
        tipo = "casa"
    elif tipo_opcao == "3":
        tipo = "estudio"
    else:
        print("Opção inválida.")
        return


    quartos = 1
    if tipo in ["apartamento", "casa"]:
        qtd_quartos = input("Deseja 2 quartos? (s/n): ").lower()
        if qtd_quartos == "s":
            quartos = 2


    garagem = False
    vagas_extra = 0


    if tipo in ["apartamento", "casa"]:
        g = input("Deseja incluir garagem? (s/n): ").lower()
        if g == "s":
            garagem = True
    elif tipo == "estudio":
        e = input("Deseja incluir estacionamento (2 vagas + R$250)? (s/n): ").lower()
        if e == "s":
            vagas_extra = int(input("Quantas vagas extras deseja além das 2 inclusas? (0 = nenhuma): "))


    criancas = input("O cliente possui crianças? (s/n): ").lower() == "s"


    aluguel = calcular_aluguel(tipo, quartos, garagem, criancas, vagas_extra)


    print("\n=== RESUMO DO ORÇAMENTO ===")
    print(f"Tipo de imóvel: {tipo.capitalize()}")
    print(f"Quartos: {quartos}")
    if tipo in ["apartamento", "casa"]:
        print(f"Garagem: {'Sim' if garagem else 'Não'}")
    elif tipo == "estudio":
        print(f"Vagas de estacionamento extras: {vagas_extra}")
    print(f"Crianças: {'Sim' if criancas else 'Não'}")
    print(f"Valor mensal do aluguel: R$ {aluguel:.2f}")
    print("Contrato imobiliário: R$ 2.000,00 (até 5x)")
    print(f"Total mensal (com contrato parcelado): R$ {aluguel + 2000/5:.2f}")


    gerar_parcelas_csv(nome, aluguel)




if __name__ == "__main__":
    main()



