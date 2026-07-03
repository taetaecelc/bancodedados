# 1. Definição das variáveis (exemplos de valores que podem ser alterados)
bateria_atual = 14       # Número inteiro de 0 a 100
bola_em_jogo = False      # Valor booleano (True ou False)

# 2. Processamento das condições com If / Elif / Else
if bateria_atual < 15 and bola_em_jogo:
    # Condição 1: Bateria abaixo de 15% E bola em jogo
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and not bola_em_jogo:
    # Condição 2: Bateria abaixo de 15% E bola parada (não em jogo)
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    # Condição 3 (Caso Geral): Bateria igual ou acima de 15%
    print("Sistema Trionda operando normalmente. Bateria ok.")
