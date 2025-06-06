#Nome: Guilherme Araujo de Carvalho
#RM: 558926
#Nome: Augusto Douglas Nogueira de Mendonça
#RM: 558371
#Nome: Vitor Augusto Franca de Oliveira
#RM: 555469


import random

# Dicionários para armazenar o score por modo de jogo
score_por_modo = {
    1: {"pontos": 0},
    2: {"pontos": 0},
    3: {"pontos": 0}
}

# Dicionário para armazenar os scores dos jogadores
scores_jogadores = {}

# Lista de perguntas
perguntas = [
    # --- Nível 1 & 2: Perguntas Fáceis ---
    {"categoria": "facil", "pergunta": "Qual o equipamento de proteção individual (EPI) que os bombeiros usam na cabeça para se proteger do calor e impactos?", "opcoes": ["a) Capacete", "b) Luva", "c) Bota", "d) Máscara"], "resposta": "a"},
    {"categoria": "facil", "pergunta": "Qual das alternativas abaixo é uma das principais causas de queimadas que não é natural?", "opcoes": ["a) Raios", "b) Calor excessivo", "c) Balões juninos", "d) Seca prolongada"], "resposta": "c"},
    {"categoria": "facil", "pergunta": "Qual é o agente extintor mais comum e eficaz para combater incêndios em vegetação, como as queimadas?", "opcoes": ["a) Gás carbônico (CO2)", "b) Pó químico", "c) Água", "d) Espuma"], "resposta": "c"},
    {"categoria": "facil", "pergunta": "Para abafar o fogo em pequenas áreas de vegetação, qual ferramenta manual é frequentemente utilizada pelo bombeiro?", "opcoes": ["a) Enxadão", "b) Pá", "c) Batedor (chicote) de incêndio", "d) Machadinha"], "resposta": "c"},
    {"categoria": "facil", "pergunta": "Qual destas ações é uma boa prática para prevenir queimadas em áreas rurais?", "opcoes": ["a) Jogar bitucas de cigarro acesas no chão", "b) Manter aceiros (faixas sem vegetação) limpos", "c) Fazer fogueiras perto de vegetação seca", "d) Queimar lixo no quintal"], "resposta": "b"},
    {"categoria": "facil", "pergunta": "A fumaça das queimadas pode causar problemas principalmente em qual parte do corpo humano?", "opcoes": ["a) Pernas", "b) Cabelos", "c) Braços", "d) Pulmões"], "resposta": "d"},
    {"categoria": "facil", "pergunta": "Qual bioma brasileiro é conhecido por ter um período de seca mais longo e, por isso, ser mais propenso a queimadas naturais e antrópicas?", "opcoes": ["a) Cerrado", "b) Mata Atlântica", "c) Amazônia", "d) Pampa"], "resposta": "a"},
    {"categoria": "facil", "pergunta": "Na maioria dos casos, fazer queimadas sem autorização é:", "opcoes": ["a) Recomendado para renovar o pasto", "b) Uma atividade inofensiva", "c) Crime ambiental", "d) Permissão para limpeza de terreno"], "resposta": "c"},
    {"categoria": "facil", "pergunta": "Quando os bombeiros jogam água diretamente nas chamas para diminuir a temperatura, eles estão usando a técnica de:", "opcoes": ["a) Abafamento", "b) Resfriamento", "c) Isolamento", "d) Contenção"], "resposta": "b"},
    {"categoria": "facil", "pergunta": "Em uma operação de combate a incêndio, qual a importância de uma boa comunicação entre os membros da equipe?", "opcoes": ["a) Apenas para socializar", "b) Para evitar acidentes e coordenar ações", "c) Para reclamar do calor", "d) Para contar piadas"], "resposta": "b"},
    {"categoria": "facil", "pergunta": "Em caso de uma queimadura leve, o que se deve fazer inicialmente?", "opcoes": ["a) Colocar manteiga", "b) Perfurar as bolhas", "c) Esfregar álcool", "d)  Lavar com água fria e corrente"], "resposta": "d"},
    {"categoria": "facil", "pergunta": "As queimadas destroem o lar e o alimento de muitos animais. Qual o resultado direto disso?", "opcoes": ["a) Aumento da população de animais", "b) Migração e morte de animais", "c) Diminuição da temperatura", "d) Crescimento de novas florestas"], "resposta": "b"},
    {"categoria": "facil", "pergunta": "Depois que as chamas são controladas, qual é a etapa importante para evitar que o fogo recomece?", "opcoes": ["a) Fazer o rescaldo, eliminando focos de calor", "b) Descansar imediatamente", "c) Ir embora do local", "d) Começar outro combate em área diferente"], "resposta": "a"},
    {"categoria": "facil", "pergunta": "Um incêndio que atinge principalmente a vegetação de florestas, matas e campos é chamado de:", "opcoes": ["a) Incêndio elétrico", "b) Incêndio veicular", "c) Incêndio florestal (ou queimada)", "d) Incêndio em edificação"], "resposta": "c"},

    # --- Nível 3 & 4: Perguntas Médias ---
    {"categoria": "medio", "pergunta": "Qual a principal função de um aceiro feito ao redor de uma propriedade rural para prevenir queimadas?", "opcoes": ["a) Criar uma barreira sem vegetação para conter o avanço do fogo", "b) Servir como estrada para veículos", "c) Ser um local para acampar", "d) Aumentar a área de plantio"], "resposta": "a"},
    {"categoria": "medio", "pergunta": "Qual destes fatores é crucial para a velocidade de propagação de uma queimada e pode mudar rapidamente?", "opcoes": ["a) Cor do solo", "b) Tipo de rocha", "c) Força e direção do vento", "d) Quantidade de pedras no caminho"], "resposta": "c"},
    {"categoria": "medio", "pergunta": "No Brasil, qual órgão federal possui uma brigada especializada no combate a incêndios florestais e atua na fiscalização ambiental?", "opcoes": ["a) Ministério da Educação", "b) Polícia Federal", "c) IBAMA (Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis)", "d) Correios"], "resposta": "c"},
    {"categoria": "medio", "pergunta": "Além dos custos diretos de combate, as queimadas geram grandes prejuízos econômicos ao:", "opcoes": ["a) Aumentar o preço da gasolina", "b) Destruir lavouras e pastagens, afetando o agronegócio", "c) Diminuir o tráfego nas estradas", "d) Aumentar o número de turistas"], "resposta": "b"},
    {"categoria": "medio", "pergunta": "Em um dia quente e com pouca umidade do ar, o risco de queimadas aumenta significativamente. Isso se deve principalmente a qual fator?", "opcoes": ["a) Maior evaporação da água", "b) Menor chance de chuva", "c) Vegetação mais seca e inflamável", "d) Presença de nuvens no céu"], "resposta": "c"},
    {"categoria": "medio", "pergunta": "Como órgãos como o INPE (Instituto Nacional de Pesquisas Espaciais) monitoram os focos de calor e auxiliam no combate às queimadas?", "opcoes": ["a) Enviando drones para cada foco", "b) Através de denúncias por telefone", "c) Enviando equipes terrestres diárias", "d) Utilizando imagens de satélite"], "resposta": "d"},
    {"categoria": "medio", "pergunta": "As grandes queimadas no Pantanal, como as de 2020, causaram a morte e o deslocamento de milhares de animais. Este evento é um exemplo de impacto em qual aspecto?", "opcoes": ["a) Apenas na economia local", "b) Principalmente na saúde humana", "c) Na biodiversidade e equilíbrio ecológico", "d) No preço dos combustíveis"], "resposta": "c"},
    {"categoria": "medio", "pergunta": "A inalação prolongada da fumaça de queimadas pode agravar ou causar quais tipos de problemas de saúde?", "opcoes": ["a) Dores de cabeça leves", "b) Problemas respiratórios graves, como asma e bronquite", "c) Queda de cabelo", "d) Crescimento excessivo de unhas"], "resposta": "b"},
    {"categoria": "medio", "pergunta": "Por que é importante que as comunidades rurais participem de programas de prevenção de queimadas e formem brigadas voluntárias?", "opcoes": ["a) Para ganhar dinheiro extra", "b) Porque são os únicos responsáveis pelo combate", "c) Para ajudar a monitorar e agir rapidamente em focos iniciais", "d) Para competir com os bombeiros oficiais"], "resposta": "c"},
    {"categoria": "medio", "pergunta": "Como a destruição da cobertura vegetal pelas queimadas afeta o solo?", "opcoes": ["a) Torna o solo mais fértil", "b) Aumenta a resistência do solo à erosão", "c) Aumenta a erosão e a perda de nutrientes", "d) Deixa o solo mais úmido"], "resposta": "c"},
    {"categoria": "medio", "pergunta": "Embora o Cerrado tenha espécies adaptadas ao fogo natural, qual o problema das queimadas de grande intensidade e frequência causadas por humanos?", "opcoes": ["a) Elas impedem a recuperação da vegetação e eliminam espécies sensíveis", "b) Elas aumentam a diversidade de espécies", "c) Elas estimulam a floração das plantas", "d) Elas melhoram a qualidade do ar"], "resposta": "a"},
    {"categoria": "medio", "pergunta": "Um bombeiro no combate a uma queimada deve estar atento à previsão do tempo, principalmente para:", "opcoes": ["a) Ver se vai chover no dia seguinte", "b) Avaliar a temperatura e a direção do vento, que afetam o fogo", "c) Saber a umidade do ar para o café da manhã", "d) Decidir o melhor horário para almoçar"], "resposta": "b"},
    {"categoria": "medio", "pergunta": "Qual o impacto a longo prazo de grandes queimadas nas florestas e no clima global?", "opcoes": ["a) Aumento da umidade do ar", "b) Contribuição para o aquecimento global devido à liberação de CO2", "c) Diminuição da poluição", "d) Crescimento de novas florestas mais rapidamente"], "resposta": "b"},
    {"categoria": "medio", "pergunta": "Após o controle de uma queimada, qual a importância da fiscalização e investigação?", "opcoes": ["a) Apenas para registrar o ocorrido", "b) Para decidir o nome da operação", "c) Para contar quantos bombeiros participaram", "d) Para identificar os responsáveis e aplicar as leis, prevenindo novas queimadas"], "resposta": "d"},

    # --- Nível 5, 6 & 7: Perguntas Difíceis ---
    {"categoria": "dificil", "pergunta": "Em situações de grandes incêndios florestais, além dos aceiros, qual técnica de combate indireto envolve a queima controlada de pequenas áreas para remover o combustível do fogo principal?", "opcoes": ["a) Resfriamento intensivo", "b) Contra-fogo (ou fogo de encontro)", "c) Abafamento por completo", "d) Inundação da área"], "resposta": "b"},
    {"categoria": "dificil", "pergunta": "O fenômeno do 'salto do fogo' em queimadas florestais é mais provável de ocorrer em quais condições?", "opcoes": ["a) Vento fraco e umidade alta", "b) Vento forte e presença de fagulhas que atravessam barreiras", "c) Terreno plano e sem vegetação", "d) Baixa temperatura ambiente"], "resposta": "b"},
    {"categoria": "dificil", "pergunta": "Além do IBAMA, que outro órgão federal possui um sistema de combate a incêndios florestais e atua na prevenção e manejo de fogo em Unidades de Conservação federais?", "opcoes": ["a) ICMBio (Instituto Chico Mendes de Conservação da Biodiversidade)", "b) Ministério da Defesa", "c) Agência Nacional de Águas (ANA)", "d) Departamento Nacional de Infraestrutura de Transportes (DNIT)"], "resposta": "a"},
    {"categoria": "dificil", "pergunta": "As queimadas de 2020 no Pantanal, embora não tenham sido as únicas, chamaram a atenção mundial pela sua extensão. Qual fator natural, além da seca prolongada, contribuiu para a intensidade desses incêndios?", "opcoes": ["a) Neve intensa", "b) Chuvas torrenciais", "c) Ventos anômalos e rajadas fortes", "d) Nevoeiro denso"], "resposta": "c"},
    {"categoria": "dificil", "pergunta": "A floresta amazônica, apesar de úmida em grande parte, sofre com incêndios que se iniciam principalmente em áreas de:", "opcoes": ["a) Lagos e rios", "b) Desmatamento e grilagem, onde o fogo é usado para 'limpar' a terra", "c) Montanhas rochosas", "d) Geleiras e picos nevados"], "resposta": "b"},
    {"categoria": "dificil", "pergunta": "Além dos impactos na agricultura e pecuária, as queimadas podem prejudicar severamente qual setor econômico fundamental para o Brasil, especialmente em biomas como o Pantanal e a Amazônia?", "opcoes": ["a) Indústria automobilística", "b) Indústria de softwares", "c) Setor de telecomunicações", "d) Turismo ecológico"], "resposta": "d"},
    {"categoria": "dificil", "pergunta": "A escala FWI (Forest Fire Weather Index) é um sistema internacional usado para avaliar o risco de incêndios florestais. Qual é o principal grupo de fatores climáticos que ela considera?", "opcoes": ["a) Luminosidade, visibilidade e pressão atmosférica", "b) Temperatura, umidade relativa do ar, velocidade do vento e quantidade de chuva", "c) Altitude, latitude e longitude", "d) Presença de nuvens, cor do céu e fase da lua"], "resposta": "b"},
    {"categoria": "dificil", "pergunta": "Em uma operação de combate a grandes incêndios florestais, como os Corpos de Bombeiros Estaduais e órgãos federais como o ICMBio e o IBAMA geralmente atuam em conjunto?", "opcoes": ["a) De forma totalmente independente, sem comunicação", "b) Apenas por meio de envio de relatórios burocráticos", "c) Competindo para ver quem chega primeiro ao local", "d) Através de forças-tarefa integradas e planos de contingência unificados"], "resposta": "d"},
    {"categoria": "dificil", "pergunta": "Além da perda direta de animais e plantas, as queimadas frequentes podem levar à 'savanização' de biomas como a Amazônia. O que isso significa?", "opcoes": ["a) Transformação em um ecossistema mais úmido e florestado", "b) Redução da biodiversidade e substituição por vegetação mais resistente ao fogo, similar à savana", "c) Aumento da área de lagos e rios", "d) Crescimento de cidades no local da floresta"], "resposta": "b"},
    {"categoria": "dificil", "pergunta": "Qual o impacto das queimadas na balança de carbono do planeta, contribuindo para o efeito estufa?", "opcoes": ["a) Liberam grandes quantidades de CO2 e outros gases na atmosfera", "b) Absorvem grandes quantidades de CO2 da atmosfera", "c) Transformam CO2 em oxigênio", "d) Não têm qualquer impacto no carbono atmosférico"], "resposta": "a"},
    {"categoria": "dificil", "pergunta": "O processo de reflorestamento em áreas degradadas por queimadas é complexo. Qual o principal desafio para a recuperação da vegetação nativa em grande escala nessas áreas?", "opcoes": ["a) Alto custo, necessidade de sementes e mudas adequadas, e tempo para o crescimento", "b) Falta de interesse da população", "c) Excesso de chuvas", "d) Dificuldade em encontrar máquinas para o plantio"], "resposta": "a"},
    {"categoria": "dificil", "pergunta": "A Lei de Crimes Ambientais (Lei nº 9.605/98) prevê penalidades para quem causa queimadas sem autorização. Quais são as principais sanções aplicáveis a esses crimes?", "opcoes": ["a) Apenas advertência verbal", "b) Multa e prisão", "c) Serviço comunitário obrigatório", "d) Curso de conscientização online"], "resposta": "b"},
]

# Função para exibir os scores
def exibir_scores():
    print("\nPONTUAÇÕES:")
    for jogador, scores in scores_jogadores.items():
        for modo, score in scores.items():
            print(f"Jogador {jogador} - Modo {modo*9} perguntas: {score} pontos")

# Função para exibir as boas vindas e pedir o nome do jogador
def boas_vindas():
    print("\nSEJA BEM-VINDO!!!")
    print("\nQual o seu nome??")
    jogador_nome = input("Meu nome é:  ")
    return jogador_nome

# Função para selecionar o modo de jogo
def selecionar_modo():
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
    if categoria == "facil":
        return 1
    elif categoria == "medio":
        return 2
    elif categoria == "dificil":
        return 3

# Função para verificar a resposta e somar os pontos
def verificar_resposta(pergunta, resposta, jogador_nome, modo):
    if pergunta["resposta"] == resposta:
        pontos = calcular_peso(pergunta["categoria"])
        print("Resposta correta! Você ganhou {} pontos.".format(pontos))
        score_por_modo[modo]["pontos"] += pontos
    else:
        print("Resposta incorreta! Nenhum ponto foi ganho.")

# Função principal do jogo
def main():
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
        perguntas_selecionadas = random.sample(perguntas, num_perguntas)

        # Iterar sobre as perguntas selecionadas
        for pergunta in perguntas_selecionadas:
            print("\nCategoria:", pergunta["categoria"])
            print("Pergunta:", pergunta["pergunta"])
            for opcao in pergunta["opcoes"]:
                print(opcao)
            while True:
                resposta = input("Digite a letra da opção correta: ").lower()
                if resposta in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("Opção inválida. Por favor, digite a letra correspondente à resposta correta (a, b, c, d).")
            verificar_resposta(pergunta, resposta, jogador_nome, modo)

        # Atualizar o score do jogador
        if jogador_nome not in scores_jogadores:
            scores_jogadores[jogador_nome] = {}
        scores_jogadores[jogador_nome][modo] = score_por_modo[modo]["pontos"]

        # Exibir pontuação final
        print(f"\nPontuação final de {jogador_nome} no modo de jogo {modo}: {score_por_modo[modo]['pontos']} pontos")

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