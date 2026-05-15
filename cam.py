historico = []

############################################################
def registrar_foto():
    print("REGISTRAR FOTO DE ANOTACAO")

    disciplina = ""
    while disciplina == "":
        disciplina = input("Disciplina: ")
        if disciplina == "":
            print("Informe a disciplina.")

    tipo = ""
    while tipo not in ["1", "2", "3"]:
        print("Material: [1] Lousa  [2] Caderno  [3] Slide")
        tipo = input("Escolha (1-3): ")
        if tipo not in ["1", "2", "3"]:
            print("Opcao invalida.")

    tipos = {"1": "Lousa", "2": "Caderno", "3": "Slide"}
    historico.append(f"Foto: {disciplina} - {tipos[tipo]}")

    print(f"Foto registrada!")
    print(f"  Disciplina : {disciplina}")
    print(f"  Material   : {tipos[tipo]}")
    input("ENTER para voltar...")

##########################################################################
def iniciar_foco():
    print("INICIAR SESSAO DE FOCO")

    minutos = 0
    while minutos < 1 or minutos > 120:
        try:
            minutos = int(input("Duracao em minutos (1-120): "))
            if minutos < 1 or minutos > 120:
                print("Valor entre 1 e 120.")
        except ValueError:
            print("Digite apenas numeros.")

    conteudo = ""
    while conteudo == "":
        conteudo = input("O que vai estudar? ").strip()
        if conteudo == "":
            print("Informe o conteudo.")

    intervalos = minutos // 25
    historico.append(f"Foco: {conteudo} - {minutos} min")

    print(f"Sessao configurada!")
    print(f"  Conteudo   : {conteudo}")
    print(f"  Duracao    : {minutos} minutos")
    print(f"  Intervalos : {intervalos} intervalo(s) de 5 min")
    input("ENTER para voltar...")

##############################################################################
def gerar_resumo():
    print("GERAR RESUMO POR MATERIA")

    banco = {
        "1": ["Matematica",  ["Derivadas", "Integrais", "Matrizes"]],
        "2": ["Portugues",   ["Coesao", "Argumentacao", "Gramatica"]],
        "3": ["Programacao", ["Variaveis", "Funcoes", "Listas"]],
        "4": ["Historia",    ["Rev. Industrial", "Guerra Fria", "Brasil Colonia"]],
    }

    print("Materias: [1] Matematica  [2] Portugues  [3] Programacao  [4] Historia")
    escolha = ""
    while escolha not in banco:
        escolha = input("Escolha (1-4): ").strip()
        if escolha not in banco:
            print("Opcao invalida.")

    nome, topicos = banco[escolha]
    historico.append(f"Resumo: {nome}")

    print(f"Resumo - {nome}:")
    for i, t in enumerate(topicos, 1):
        print(f"  {i}. {t}")
    input("ENTER para voltar...")

##############################################################
def ver_historico():
    print("HISTORICO DA SESSAO")
    if len(historico) == 0:
        print("Nenhuma acao registrada.")
    else:
        for i, item in enumerate(historico, 1):
            print(f"  {i}. {item}")
    input("ENTER para voltar...")

##############################################################################
def main():
    print("  JOVI CamStudy | FIAP Challenge 2026")

    while True:
        print("[1] Registrar Foto de Anotacao")
        print("[2] Iniciar Sessao de Foco")
        print("[3] Gerar Resumo por Materia")
        print("[4] Ver Historico")
        print("[0] Sair")

        opcao = input("Opcao: ").strip()

        match opcao:
            case "1": registrar_foto()
            case "2": iniciar_foco()
            case "3": gerar_resumo()
            case "4": ver_historico()
            case "0":
                print("Encerrando. Bons estudos!")
                break
            case _:
                print("Opcao invalida.")

if __name__ == "__main__":
    main()