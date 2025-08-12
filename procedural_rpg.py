import random

MAP_SIZE = 4  # Define o tamanho do mapa quadrado 4x4

# Constantes representando os tipos de salas do mapa
SALA_VAZIA = "Vazia"
SALA_INIMIGO = "Inimigo"
SALA_ITEM = "Item"
SALA_TESOURO = "Tesouro"
SALA_SAIDA = "Saida"

class Jogador:
    def __init__(self):
        # Atributos básicos do jogador
        self.hp = 100
        self.max_hp = 100
        self.ataque = 20
        self.defesa = 10
        self.inventario = {"Poção": 2}
        self.posicao = (0, 0)  # Posição inicial no mapa
        self.espada_rara = False  # Flag para controle do objetivo principal

    def atacar(self, inimigo):
        # Calcula o dano considerando defesa do inimigo, sem dano negativo
        dano = max(0, self.ataque - inimigo.defesa)
        inimigo.hp -= dano
        print(f"Você causou {dano} de dano no inimigo!")

    def defender(self):
        # Indica que o jogador está em modo de defesa para reduzir dano
        print("Você se defende e reduz o dano do próximo ataque!")

    def usar_item(self):
        # Usa uma poção do inventário, recuperando HP se disponível
        if self.inventario.get("Poção", 0) > 0:
            cura = 30
            self.hp = min(self.max_hp, self.hp + cura)
            self.inventario["Poção"] -= 1
            print(f"Você usou uma Poção e recuperou {cura} HP!")
        else:
            print("Você não tem poções!")

class Inimigo:
    def __init__(self):
        # Inimigo com atributos aleatórios para variar desafios
        self.hp = random.randint(50, 80)
        self.ataque = random.randint(10, 15)
        self.defesa = random.randint(5, 8)

    def atacar(self, jogador):
        # Calcula dano causado ao jogador considerando sua defesa
        dano = max(0, self.ataque - jogador.defesa)
        jogador.hp -= dano
        print(f"Inimigo causou {dano} de dano em você!")

def criar_mapa():
    # Inicializa o mapa com salas vazias
    mapa = [[SALA_VAZIA for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

    # Define posições aleatórias para a saída e o tesouro, garantindo que não coincidam
    saida_pos = (random.randint(0, MAP_SIZE-1), random.randint(0, MAP_SIZE-1))
    tesouro_pos = (random.randint(0, MAP_SIZE-1), random.randint(0, MAP_SIZE-1))
    while tesouro_pos == saida_pos:
        tesouro_pos = (random.randint(0, MAP_SIZE-1), random.randint(0, MAP_SIZE-1))

    mapa[saida_pos[0]][saida_pos[1]] = SALA_SAIDA
    mapa[tesouro_pos[0]][tesouro_pos[1]] = SALA_TESOURO

    # Distribui inimigos e itens aleatoriamente no restante do mapa
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if (i, j) in [saida_pos, tesouro_pos]:
                continue
            chance = random.random()
            if chance < 0.3:
                mapa[i][j] = SALA_INIMIGO
            elif chance < 0.5:
                mapa[i][j] = SALA_ITEM

    return mapa

def mostrar_mapa(mapa, jogador):
    # Exibe o mapa com a posição atual do jogador marcada; outras salas permanecem ocultas
    print("\nMapa (posição atual marcada com X):")
    for i in range(MAP_SIZE):
        linha = ""
        for j in range(MAP_SIZE):
            linha += " X " if (i, j) == jogador.posicao else " ? "
        print(linha)
    print()

def combate(jogador, inimigo):
    defendendo = False
    # Loop de combate até que jogador ou inimigo sejam derrotados
    while inimigo.hp > 0 and jogador.hp > 0:
        print(f"\nSeu HP: {jogador.hp} | Inimigo HP: {inimigo.hp}")
        print("Escolha sua ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Usar Item")
        print("4 - Fugir")

        escolha = input("> ")
        if escolha == "1":
            jogador.atacar(inimigo)
            defendendo = False
        elif escolha == "2":
            jogador.defender()
            defendendo = True
        elif escolha == "3":
            jogador.usar_item()
            defendendo = False
        elif escolha == "4":
            # Chance de fuga bem-sucedida
            if random.random() > 0.5:
                print("Você fugiu com sucesso!")
                return False
            else:
                print("Fuga falhou!")
                defendendo = False
        else:
            print("Opção inválida.")
            continue

        # Inimigo ataca caso ainda esteja vivo; dano é reduzido se jogador está defendendo
        if inimigo.hp > 0:
            defesa_efetiva = jogador.defesa * 2 if defendendo else jogador.defesa
            dano_ataque = max(0, inimigo.ataque - defesa_efetiva)
            jogador.hp -= dano_ataque
            print(f"Inimigo atacou e causou {dano_ataque} de dano!")

    # Resultado do combate
    if jogador.hp <= 0:
        print("Você foi derrotado... Fim de jogo.")
        return True
    else:
        print("Inimigo derrotado!")
        return True

def jogo():
    mapa = criar_mapa()
    jogador = Jogador()

    print("Bem-vindo ao RPG Procedural 4x4!")
    print("Objetivo: encontre a espada rara e depois a saída.\n")

    while True:
        mostrar_mapa(mapa, jogador)
        print(f"Você está na posição {jogador.posicao}.")
        print("Escolha para onde mover:")
        print("w - cima | s - baixo | a - esquerda | d - direita")

        move = input("> ").lower()
        x, y = jogador.posicao

        # Atualiza posição com base no input, validando limites do mapa
        if move == "w" and x > 0:
            jogador.posicao = (x-1, y)
        elif move == "s" and x < MAP_SIZE-1:
            jogador.posicao = (x+1, y)
        elif move == "a" and y > 0:
            jogador.posicao = (x, y-1)
        elif move == "d" and y < MAP_SIZE-1:
            jogador.posicao = (x, y+1)
        else:
            print("Movimento inválido.")
            continue

        sala = mapa[jogador.posicao[0]][jogador.posicao[1]]
        print(f"\nVocê entrou em uma sala: {sala}")

        if sala == SALA_INIMIGO:
            inimigo = Inimigo()
            venceu = combate(jogador, inimigo)
            if not venceu:
                print("Você escapou do combate.")
            elif jogador.hp <= 0:
                print("Game Over!")
                break
            else:
                # Remove inimigo da sala ao ser derrotado
                mapa[jogador.posicao[0]][jogador.posicao[1]] = SALA_VAZIA

        elif sala == SALA_ITEM:
            itens = ["Poção", "Poção de Mana", "Espada Curta", "Escudo de Bronze", "Armadura de Couro"]
            item = random.choice(itens)
            print(f"Você encontrou um item: {item}!")
            jogador.inventario[item] = jogador.inventario.get(item, 0) + 1

            # Aplica efeitos imediatos para alguns itens
            if item == "Poção":
                print("Você usou uma Poção e recuperou 30 HP!")
                jogador.hp = min(jogador.max_hp, jogador.hp + 30)
            elif item == "Espada Curta":
                print("Você encontrou uma espada curta! +5 de ataque")
                jogador.ataque += 5
            elif item == "Escudo de Bronze":
                print("Você encontrou um escudo de bronze! +3 de defesa")
                jogador.defesa += 3
            elif item == "Armadura de Couro":
                print("Você encontrou uma armadura de couro! +2 de defesa")
                jogador.defesa += 2
            elif item == "Poção de Mana":
                print("Você encontrou uma poção de mana! +20 de mana (não implementado)")

            mapa[jogador.posicao[0]][jogador.posicao[1]] = SALA_VAZIA

        elif sala == SALA_TESOURO:
            print("Parabéns! Você encontrou a espada rara!")
            jogador.espada_rara = True
            mapa[jogador.posicao[0]][jogador.posicao[1]] = SALA_VAZIA

        elif sala == SALA_SAIDA:
            if jogador.espada_rara:
                print("Você encontrou a saída com a espada rara. Você venceu o jogo!")
                break
            else:
                print("Você encontrou a saída, mas ainda não tem a espada rara. Continue procurando!")

        elif sala == SALA_VAZIA:
            print("Sala vazia... siga em frente.")

        # Verifica condição de derrota após ações na sala
        if jogador.hp <= 0:
            print("Você morreu. Fim de jogo.")
            break

if __name__ == "__main__":
    jogo()
