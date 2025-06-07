#Nome: Guilherme Araujo de Carvalho
#RM: 558926
#Nome: Augusto Douglas Nogueira de Mendonça
#RM: 558371
#Nome: Vitor Augusto Franca de Oliveira
#RM: 555469


import random
import json
import os

# Dicionários para armazenar o score por modo de jogo
score_por_modo = {
    1: {"pontos": 0},
    2: {"pontos": 0},
    3: {"pontos": 0}
}



with open("dados.json", 'r', encoding='utf-8') as arquivo:
    dic = json.load(arquivo)

# Função para exibir os scores
def exibir_scores():
    """
    Exibe as pontuações dos jogadores por modo de jogo a partir do dicionário 'dic'.
    """
    print("\nPONTUAÇÕES:")
    for jogador, scores in dic["Pontuacoes"].items():
        for modo, score in scores.items():
            print(f"Jogador {jogador} - Modo {modo} perguntas: {score} pontos")

# Função para exibir as boas vindas e pedir o nome do jogador
def boas_vindas():
    """
    Exibe uma mensagem de boas-vindas e solicita o nome do jogador.

    Returns:
        str: Nome do jogador inserido pelo usuário.
    """
    print("\nSEJA BEM-VINDO!!!")
    print("\nQual o seu nome??")
    jogador_nome = input("Meu nome é:  ")
    return jogador_nome

# Função para selecionar o modo de jogo
def selecionar_modo():
    """
    Exibe as opções de modo de jogo e solicita ao jogador que escolha uma.

    Returns:
        int: Modo de jogo selecionado (1, 2 ou 3).
    """
    while True:
        print("\nSelecione o modo de jogo:")
        print("1 - 9 perguntas")
        print("2 - 18 perguntas")
        print("3 - 27 perguntas")
        try:
            modo = int(input("Digite o número correspondente ao modo desejado: "))
            if modo in [1, 2, 3]:
                return modo
            else:
                print("Opção inválida. Por favor, selecione 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Função para calcular o peso da pergunta com base na categoria
def calcular_peso(categoria):
    """
    Retorna o valor em pontos com base na dificuldade da pergunta.

    Args:
        categoria (str): Dificuldade da pergunta ("facil", "medio" ou "dificil").

    Returns:
        int: Peso em pontos da pergunta.
    """
    if categoria == "facil":
        return 1
    elif categoria == "medio":
        return 2
    elif categoria == "dificil":
        return 3

# Função para verificar a resposta e somar os pontos
def verificar_resposta(pergunta, resposta, jogador_nome, modo):
    """
    Verifica se a resposta do jogador está correta, soma os pontos conforme a dificuldade
    e exibe uma mensagem ao jogador.

    Args:
        pergunta (str): Texto da pergunta.
        resposta (str): Resposta fornecida pelo jogador.
        jogador_nome (str): Nome do jogador.
        modo (int): Modo de jogo atual.
    """
    if dic["Perguntas"][pergunta]["resposta"] == resposta:
        pontos = calcular_peso(dic["Perguntas"][pergunta]["dificuldade"])
        print("Resposta correta! Você ganhou {} pontos.".format(pontos))
        score_por_modo[modo]["pontos"] += pontos
    else:
        print("Resposta incorreta! Nenhum ponto foi ganho.")

# Função principal do jogo
def main():
    """
    Função principal do jogo. Controla o fluxo do jogo:
    exibe menus, lê dados do jogador, sorteia perguntas,
    verifica respostas, atualiza e salva pontuações.
    """
    while True:
        print("\n===  ===")
        print("\n=== Queimadas Quiz: Desvendando os Mistérios Queimadas ===")
        exibir_scores()
        jogador_nome = boas_vindas()

        # Inicializar ou resetar os scores para o novo jogador
        score_por_modo[1]["pontos"] = 0
        score_por_modo[2]["pontos"] = 0
        score_por_modo[3]["pontos"] = 0

        modo = selecionar_modo()

        # Selecionar perguntas proporcionalmente ao modo de jogo
        num_perguntas = modo * 9
        perguntas_selecionadas = random.sample(list(dic["Perguntas"].keys()), num_perguntas)

        # Iterar sobre as perguntas selecionadas
        for pergunta in perguntas_selecionadas:
            print("\nCategoria:", dic["Perguntas"][pergunta]["dificuldade"])
            print("Pergunta:", pergunta)
            for opcao in dic["Perguntas"][pergunta]["opcoes"]:
                print(opcao)
            while True:
                resposta = input("Digite a letra da opção correta: ").lower()
                if resposta in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("Opção inválida. Por favor, digite a letra correspondente à resposta correta (a, b, c, d).")
            os.system('cls')
            verificar_resposta(pergunta, resposta, jogador_nome, modo)

        # Atualizar o score do jogador
        if jogador_nome not in dic["Pontuacoes"]:
            dic["Pontuacoes"][jogador_nome] = {}

        # Salvar pontuação final
        dic["Pontuacoes"][jogador_nome][modo] = score_por_modo[modo]["pontos"]
        # Exibir pontuação final
        print(f"\nPontuação final de {jogador_nome} no modo de jogo {modo}: {score_por_modo[modo]['pontos']} pontos")

        with open('dados.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dic, arquivo, indent=4)

        # Perguntar ao jogador se deseja jogar novamente
        while True:
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
            if jogar_novamente in ['s', 'n']:
                break
            else:
                print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break

# Executar o jogo
if __name__ == "__main__":
    main()