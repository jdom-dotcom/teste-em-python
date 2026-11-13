import random

class Jogador:
    def __init__(self, nome_da_lenda, classe):
        self.nome = nome_da_lenda
        self.classe = classe
        self.nivel = 1
        self.experiencia = 0
        self.ouro = 0
        self.inventario = []

        if classe == "Guerreiro":
            self.vida_max = 300
            self.vida_atual = 300
            self.dano_base = 30
            self.habilidade = "Corte Céu Limpo"
            self.custo_da_habilidade = 75
            self.carga_base = 75
            self.carga_max = 150

        elif classe == "Mago":
            self.vida_max = 150
            self.vida_atual = 150
            self.dano_base = 40
            self.habilidade = "Último Prisma"
            self.custo_da_habilidade = 100
            self.carga_base = 150
            self.carga_max = 200

        elif classe == "Arqueiro":
            self.vida_max = 220
            self.vida_atual = 220
            self.dano_base = 20
            self.habilidade = "Iron Rain"
            self.custo_da_habilidade = 25
            self.carga_base = 100
            self.carga_max = 150
        else:
            raise ValueError("Classe inválida")

    def receber_dano(self, dano):
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0

    def usar_habilidade(self, alvo):
        if self.carga_base >= self.custo_da_habilidade:
            self.carga_base -= self.custo_da_habilidade
            dano = self.dano_base * 2
            alvo.receber_dano(dano)
            print(f"\n⚡ {self.nome} usou {self.habilidade}! Causou {dano} de dano!")
            return True
        else:
            print(f"\n❌ Carga insuficiente! Precisa de {self.custo_da_habilidade}, você tem {self.carga_base}")
            return False

    def ataque_basico(self, alvo):
        dano = self.dano_base + random.randint(-5, 10)
        alvo.receber_dano(dano)
        print(f"\n⚔️ {self.nome} atacou! Causou {dano} de dano!")

    def status(self):
        print(f"\n{'='*50}")
        print(f"Nome: {self.nome} | Nível: {self.nivel}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida_atual}/{self.vida_max}")
        print(f"Carga: {self.carga_base}/{self.carga_max}")
        print(f"Ouro: {self.ouro} | Experiência: {self.experiencia}")
        print(f"{'='*50}")

class Inimigo:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida_max = vida
        self.vida_atual = vida
        self.dano = dano

    def receber_dano(self, dano):
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0

    def ataque_basico(self, alvo):
        dano = self.dano + random.randint(-5, 5)
        alvo.receber_dano(dano)
        print(f"🗡️ {self.nome} atacou! Causou {dano} de dano!")

    def esta_vivo(self):
        return self.vida_atual > 0

def combate(jogador, inimigo):
    print(f"\n{'='*50}")
    print(f"⚔️ COMBATE INICIADO!")
    print(f"{jogador.nome} vs {inimigo.nome}")
    print(f"{'='*50}")

    while jogador.vida_atual > 0 and inimigo.vida_atual > 0:
        print(f"\nVida do {jogador.nome}: {jogador.vida_atual}/{jogador.vida_max}")
        print(f"Vida do {inimigo.nome}: {inimigo.vida_atual}/{inimigo.vida_max}")
        print("\n--- Sua ação ---")
        print("1 - Ataque básico")
        print("2 - Usar habilidade")
        print("3 - Fugir")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            jogador.ataque_basico(inimigo)
        elif escolha == "2":
            jogador.usar_habilidade(inimigo)
        elif escolha == "3":
            if random.random() > 0.5:
                print(f"\n🏃 {jogador.nome} conseguiu fugir!")
                return False
            else:
                print(f"\n❌ Não conseguiu fugir!")
        else:
            print("❌ Opção inválida!")
            continue

        if not inimigo.esta_vivo():
            print(f"\n🎉 {inimigo.nome} foi derrotado!")
            jogador.ouro += 50
            jogador.experiencia += 100
            return True

        inimigo.ataque_basico(jogador)

        if not jogador.esta_vivo():
            print(f"\n💀 {jogador.nome} foi derrotado!")
            return False

    return False

def menu_principal(jogador):
    while True:
        print(f"\n{'='*50}")
        print("MENU PRINCIPAL")
        print(f"{'='*50}")
        print("1 - Ver status")
        print("2 - Inventário")
        print("3 - Explorar dungeon")
        print("4 - Descansar (recuperar vida)")
        print("5 - Sair do jogo")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            jogador.status()
        elif escolha == "2":
            mostrar_inventario(jogador)
        elif escolha == "3":
            explorar_dungeon(jogador)
        elif escolha == "4":
            jogador.vida_atual = jogador.vida_max
            jogador.carga_base = jogador.carga_max
            print("✨ Você descansou e recuperou toda sua vida e carga!")
        elif escolha == "5":
            print("Até logo, aventureiro!")
            break
        else:
            print("❌ Opção inválida!")

def mostrar_inventario(jogador):
    print(f"\n{'='*50}")
    print("INVENTÁRIO")
    print(f"{'='*50}")
    if len(jogador.inventario) == 0:
        print("Seu inventário está vazio.")
    else:
        for i, item in enumerate(jogador.inventario, 1):
            print(f"{i} - {item}")
    print(f"Ouro: {jogador.ouro}")

def explorar_dungeon(jogador):
    print(f"\n{'='*50}")
    print("🏰 EXPLORANDO A DUNGEON")
    print(f"{'='*50}")
    
    inimigos = [
        Inimigo("Goblin", 50, 10),
        Inimigo("Orc", 80, 15),
        Inimigo("Dragão Menor", 150, 25),
    ]

    inimigo = random.choice(inimigos)
    print(f"Você encontrou um {inimigo.nome}!")

    if combate(jogador, inimigo):
        print("✨ Combate vencido!")
    else:
        print("💀 Você foi derrotado...")

# INÍCIO DO JOGO
print("=" * 50)
print("BEM VINDO AO DUNGEON QUEST")
print("=" * 50)

nome_da_lenda = input("Escolha o nome do seu personagem: ").strip()
print(f"Perfeito, seu nome é: {nome_da_lenda}")

while True:
    print("\nAgora escolha sua classe digitando 1, 2 ou 3:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")

    escolha = input("Digite o número da sua classe: ").strip()

    if escolha == "1":
        classe_escolhida = "Guerreiro"
        break
    elif escolha == "2":
        classe_escolhida = "Mago"
        break
    elif escolha == "3":
        classe_escolhida = "Arqueiro"
        break
    else:
        print("Apenas números de 1 a 3. Tente novamente.")

jogador = Jogador(nome_da_lenda, classe_escolhida)

print("\n✨ Personagem criado com sucesso!")
jogador.status()
print("\nVamos começar sua aventura!")

menu_principal(jogador)