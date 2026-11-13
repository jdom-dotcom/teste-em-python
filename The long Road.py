
from random import randint
import sys
import time

import random

class Item:
    def __init__(self, nome, dano_min, dano_max,municao_min,municao_max):
        self.nome = nome
        self.dano = random.randint(dano_min, dano_max)
        self.municao_min = municao_min
        self.municao_max = municao_max
        self.municao_atual = random.randint(municao_min, municao_max)
        self.quantidade = 1

    def usar(self):
        if self.municao_atual <= 0:
            print(f"{self.nome} está sem balas")
            time.sleep(1)
            return False

        self.municao_atual = max(0,self.municao_atual - 1)
        if self.municao_atual ==0:
            print(f'{self.nome} Está sem balas')
            time.sleep(1)

        return True

    def __str__(self):
        if self.dano>0:
            return f"{self.nome} | Dano: {self.dano} | Muniçã/Durabilidade: {self.municao_min}/{self.municao_max}"
        else:
            return f'{self.nome} (x{self.quantidade})'

       
class Carro:

    def __init__(self, motor,jogador):
        self.jogador = jogador
        self.motor = motor
        self.distancia_total = 200
        self.distancia_percorrida = 0
        self.quantidade_max = 60
        self.tanques = {
            'Gasolina': 0,
            'Diesel': 0,
            'Etanol':6
        }
        # oleo de cozinha
        self.oleo_max = 6
        self.oleo_atual = 6
        #beba agua!!!
        self.agua_max = 10
        self.agua_atual = 10
        #TEnis do carro
        self.pneu_vida = 100.0
        self.gasto_pneu_base = 2
        # Configura o motor inicial
        self.configurar_motor(motor)

    def configurar_motor(self, motor):
        if motor == "V8_turbo_diesel":
            self.motor = motor
            self.velocidade_maxima = 10
            self.taxa_de_consumo = 1.5
            self.tipo_combustivel = ["Diesel"]
            self.taxa_oleo = 0.5
            self.taxa_agua = 0.75

        elif motor == "v6_carburado":
            self.motor = motor
            self.velocidade_maxima = 5
            self.taxa_de_consumo = 1
            self.tipo_combustivel = ["Gasolina"]
            self.taxa_oleo = 0.25
            self.taxa_agua = 0.5

        elif motor == "v3_aspirado|motor_hibrido(Motor de KWID)":
            self.motor = motor
            self.velocidade_maxima = 1
            self.taxa_de_consumo = 0.5
            self.tipo_combustivel = ["Etanol", "Gasolina"]
            self.taxa_oleo = 0.1
            self.taxa_agua = 0.25

        else:
            raise ValueError("Carro sem motor definido")
    def consumo_fluidos(self):
        self.oleo_atual = max(0,round(self.oleo_atual - self.taxa_oleo, 2))
        self.agua_atual = max(0,round(self.agua_atual - self.taxa_agua, 2))

        if self.oleo_atual<= 0:
            print('\n'*7)
            print('='*50)
            print('---> GAME OVER <---')
            print('='*50)
            print('\n'*7)
            time.sleep(2)
            print(f'(O motor Fundiu por falta de ÓLEO. Os zumbis alcançaram e dovoraram {self.jogador.nome})\n')
            sys.exit()
        if self.agua_atual <= 0:
            print('\n'*7)
            print('='*50)
            print('---> GAME OVER <---')
            print('='*50)
            print('\n'*7)
            time.sleep(2)
            print(f'(Radiador ferveu e o motor explodiu. {self.jogador.nome} ficou em pedaços)\n')
            sys.exit()

    def trocar_motor(self, novo_motor):
        # Troca o motor
        self.configurar_motor(novo_motor)

        print('-.'*25)
        print(f" Motor bomba trocado para: {self.motor}")
        print(f" Velocidade máxima: {self.velocidade_maxima}")
        print(f" movido á: {self.tipo_combustivel}")
        print('-.'*25)

    def abastecer(self, tipo_combustivel, quantidade):
        
        # Verifica qual combustível está sendo usado
        if tipo_combustivel not in self.tanques:
            raise ValueError ("Combustivel invalido")

        self.tanques[tipo_combustivel] += quantidade
        self.tanques[tipo_combustivel] = min(
            self.tanques[tipo_combustivel],
            self.quantidade_max
        )

    def consumo_combustivel (self):
        combustivel_gasto = self.taxa_de_consumo
        self.consumo_fluidos()
        if len(self.tipo_combustivel) == 1:
            combustivel = self.tipo_combustivel [0]
            if self.tanques[combustivel] >= combustivel_gasto:
                self.tanques[combustivel] -= combustivel_gasto
            else:
                self.tanques[combustivel] = 0
                print('\n'*7)
                print("=" * 50)
                print(" ----> GAME OVER <----")
                print("=" * 50)
                print('\n'*7)
                time.sleep(2)
                print(f"({self.jogador.nome} Morreu no caminho ficando sem combustível)\n")
                sys.exit()
        else:
            if self.tanques['Gasolina'] >= combustivel_gasto:
                self.tanques['Gasolina'] -= combustivel_gasto
            elif self.tanques['Etanol']>= combustivel_gasto:
                self.tanques['Etanol']-=combustivel_gasto
            else:
                print('\n'*7)
                print("=" * 50)
                print(" ----> GAME OVER <----")
                print("=" * 50)
                print('\n'*7)
                time.sleep(2)
                print(f"({self.jogador.nome}) Morreu no Caminho ficando sem combustível)\n")
                print('\n')
                sys.exit() 
                
    def mover(self):
        distancia = self.velocidade_maxima
        self.distancia_restante = (self.distancia_total - self.distancia_percorrida)
        distancia = min(distancia,self.distancia_restante) 
        self.distancia_percorrida += distancia

        print('Viajando...')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        gasto_pneu_final = self.gasto_pneu_base
        if random.randint(1,100) <= 25:
            obstaculos = ["Pedaços de metal","Escombro de barricada","Buraco","Espinhos na pista"]
            obs_sorteado = random.choice(obstaculos)
            dano_extra_pneu = random.randint(5,20)
            gasto_pneu_final += dano_extra_pneu
            print('\n'*7)
            print('-.'*25)
            print('OBSTÁCULO NA PISTA!')
            print('-.'*25)
            print('\n'*7)
            time.sleep(2)
            print(f'Você passou por cima de um ({obs_sorteado})!')
            time.sleep(1)
            print(f'-{dano_extra_pneu}% de integridade do Pneu')
            time.sleep(2)
        self.pneu_vida = max(0.0, round(self.pneu_vida - gasto_pneu_final, 1))

        self.consumo_combustivel()
        
        print(f'Você dirigiu {distancia} Km')    
        print(f'Distancia Percorrida: {self.distancia_percorrida}/{self.distancia_total} Km')
        print(f'Desgate do Pneu: - {self.gasto_pneu_base}%')
        print('\n'*11)
        time.sleep(2)
        if self.pneu_vida <= 0:
            print('\n'*7)
            print("=" * 50)
            print(" ----> GAME OVER <----")
            print("=" * 50)
            print('\n'*7)
            time.sleep(2)
            print(f'(O pneu do estorou em alta velocidade! O carro capotou... e {self.jogador.nome} não resisistiu)\n')
            sys.exit()
        if self.distancia_percorrida >= self.distancia_total:
            print('\n' + '='*50)
            print('Parabens você consegui')
            print('\n' + '='*50)
            return True

        return False    
        
        
                


            
# receita para fazer galão de combustível: galão de gasolina = tipo de combustível = gasolina.

class Jogador:
    def __init__(self, nome_da_lenda):
        self.nome = nome_da_lenda
        self.vida_max = 200
        self.vida_atual = 200
        self.defesa_max = 300
        self.defesa_atual = 0
        self.inventario = Inventario(50)
        self.item_equipado = None

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa_atual)
        self.defesa_atual = max(0, self.defesa_atual - dano)
        self.vida_atual -= dano_final

        if self.vida_atual <= 0:
            self.vida_atual = 0
            print('\n'*7)
            print("=" * 50)
            print(" ----> GAME OVER <----")
            print("=" * 50)
            print('\n'*7)
            time.sleep(3)
            print(f"({self.nome} tentou abraçar um zumbi)\n")
            sys.exit()

    def ataque_basico(self, alvo):
        dano_item = 0

        if self.item_equipado:
            if self.item_equipado.municao_atual <=0:
                print(f'{self.item_equipado.nome} está sem munição')
                time.sleep(1)

            else:
                dano_item = self.item_equipado.dano
                self.item_equipado.usar()

        dano = 15 + dano_item + randint(-5, 20)
        alvo.receber_dano(dano)
        print('-'*50)
        print(f"\n{self.nome} atacou! Dano:{dano}")
        time.sleep(1)

    def esta_vivo(self):
        return self.vida_atual > 0

    def status(self):
        print('='*50)
        print(self.nome)
        print('='*50)
        print(f'Proteção: {self.defesa_atual}|{self.defesa_max}')
        print(f'Vida: {self.vida_atual}|{self.vida_max}')
        if self.item_equipado:
            if self.item_equipado.dano >0:
                print(f'Item equipado:{self.item_equipado.nome}(Munição:{self.item_equipado.municao_atual}/{self.item_equipado.max_municao if hasattr(self.item_equipado,'max_municao') else self.item_equipado.municao_max})')
            else:
                print(f'Item equipado: {self.item_equipado.nome}')
        else:
            print('Nada equipado')
        print('\n'*10)
        time.sleep(2)

class Inventario:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = []

    def adicionar(self, novo_item):
        if novo_item.dano == 0:
            for item in self.itens:
                if item.nome == novo_item.nome:
                    item.quantidade += 1
                    print(f'Você pegou:{novo_item.nome} (Total:{item.quantidade})')
                    return True

        if len(self.itens) >= self.capacidade:
            print("\n Inventário cheio!")
            return False

        self.itens.append(novo_item)
        print(f"\nVocê pegou: {novo_item.nome}")
        return True

    def remover(self, item):
        if item in self.itens:
            item.quantidade -= 1
            if item.quantidade <= 0:
                self.itens.remove(item)

    def mostrar(self, jogador_ref=None):
        
        print("=" * 50)
        print("INVENTÁRIO")
        print("=" * 50)

        if not self.itens:
            print("Inventário vazio.")
            print('\n'*12)
            time.sleep(2)
            return

        for i, item in enumerate(self.itens, 1):
            if jogador_ref and jogador_ref.item_equipado ==item:
                print(f"{i} - <o> {item}")
            else:
                print(f'{i} - {item}')

        print("0 - Sair")
        print('\n'*8)

# INVENTÁRIO DO JOGADOR

def inventario(jogador, carro):

    while True:

        jogador.inventario.mostrar(jogador_ref=jogador)

        if not jogador.inventario.itens:
            return

        escolha = input("Escolha o item: ").strip()
        

        if escolha == "0":
            return

        if not escolha.isdigit():
            print("Apenas números.")
            continue

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(jogador.inventario.itens):
            print("Item inválido.")
            continue

        item = jogador.inventario.itens[indice]
        print('-'*50)
        print(f"\nSelecionado: {item}")
        print('-'*50)
        print("1 - Equipar/Usar")
        print("2 - Voltar")
        print('3 - Remover/Descartar')
        print('\n'*9)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            if item.dano> 0:
                if jogador.item_equipado is item:
                    print(f"Este item já está equipado")
                    time.sleep(2)
                else:
                    jogador.item_equipado = item
                    print(f'|Você equipou|> <o> {item.nome}!')
            else:
                if item.nome == 'Gasolina':
                    if carro.tanques['Gasolina'] >= carro.quantidade_max:
                        print('Tanque de Gasolina cheio')
                        time.sleep(2)
                        continue
                    else:
                        carro.abastecer('Gasolina', 6)
                        print('Você usou galão de Gasolina no carro! + 6L')
                        jogador.inventario.remover(item)
                        time.sleep(2)
                        

                elif item.nome == 'Etanol':
                    if carro.tanques['Etanol'] >= carro.quantidade_max:
                        print('Tanque de Etanol cheio')
                        time.sleep(2)
                        continue
                    else:
                        carro.abastecer('Etanol',9)
                        print('Você usou galão de Etanol no carro! + 9L')
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == 'Diesel':
                    if carro.tanques['Diesel'] >= carro.quantidade_max:
                        print('Tanque de Diesel está cheio')
                        time.sleep(2)
                        continue
                    else:
                        carro.abastecer('Diesel',6)
                        print('Você usou galão de Diesel no carro! + 6L')
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Agua":
                    if carro.agua_atual>= carro.agua_max:
                        print('O radiador já está completado')
                        time.sleep(2)
                        continue
                    else:
                        carro.agua_atual = min(carro.agua_max, carro.agua_atual + 3)
                        print("Você completou 3L de Água no radiador!")
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Oleo":
                    if carro.oleo_atual >= carro.oleo_max:
                        print('O nivel de Óleo no motor já está no máximo!')
                        time.sleep(2)
                        continue
                    else:
                        carro.oleo_atual = min(carro.oleo_max, carro.oleo_atual + 1.5)
                        print("Você Abasteceu o Oleo motor! + 1,5L")
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Pneu":
                    if carro.pneu_vida >= 100.0:
                        print('Seus pneus já estão em perfeito estado')
                        time.sleep(2)
                        continue
                    else:
                        carro.pneu_vida = min(100.0, carro.pneu_vida + 50.0)
                        print('Você trocou o pneu! + 50% ' 'de integridade.')
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Comida":
                    if jogador.vida_atual >= jogador.vida_max:
                        print('sua vida está cheia')
                        time.sleep(2)
                        continue
                    else:
                        jogador.vida_atual = min(jogador.vida_max, jogador.vida_atual + 50)
                        print('Você comeu a ração e recuperou 50 de Vida!')
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Kit medico":
                    if jogador.vida_atual >= jogador.vida_max:
                        print('sua vida está cheia')
                        time.sleep(2)
                        continue
                    else:
                        jogador.vida_atual = min(jogador.vida_max, jogador.vida_atual + 100)
                        print("Você usou o Kit Médico e recuperou 100 de Vida!")
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Colete":
                    if jogador.defesa_atual >= jogador.defesa_max:
                        print('\n Sua proteção está no máximo')
                        time.sleep(2)
                        continue
                    else:
                        jogador.defesa_atual = min(jogador.defesa_max, jogador.defesa_atual + 75)
                        print("Você equipou o Colete! +75 de Proteção.")
                        jogador.inventario.remover(item)
                        time.sleep(2)

                elif item.nome == "Caixa de Motor":
                    print("Abrindo a Caixa de Motor..")
                    time.sleep(2)
                    motores_possiveis=['V8_turbo_diesel','v6_carburado','v3_aspirado|motor_hibrido(Motor de KWID)']
                    motor_sorteador = random.choice(motores_possiveis)
                    print(f'Você encontrou um motor:{motor_sorteador}')
                    carro.trocar_motor(motor_sorteador)
                    jogador.inventario.remover(item)
                    time.sleep(2)
                    continue
                else:
                    print('Item misterioso... sem utilidade por enquanto')
        elif opcao == '2':
            continue
        elif opcao == '3':
            if jogador.item_equipado is item:
                jogador.item_equipador = None
                print(f'Você desequipou {item.nome}')
                time.sleep(1)
            jogador.inventario.itens.remove(item)
            print(f'Você descatou {item.nome} do seu inventário')
            time.sleep(1)
                

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
        dano = self.dano + randint(-5, 15)
        alvo.receber_dano(dano)
        time.sleep(1)
        print(f"{self.nome} atacou! Dano:{dano}")
        print('-'*50)

    def esta_vivo(self):
        return self.vida_atual > 0


def combate(jogador, inimigo, carro):
    print('\n'*6)
    print(f"\n{'='*50}")
    print("COMBATE INICIADO!")
    print(f"{jogador.nome} vs {inimigo.nome}")
    print(f"{'='*50}\n")
    print('\n'*7)
    time.sleep(1)

    while jogador.esta_vivo() and inimigo.esta_vivo():
        print('\n'*2)
        print('='*50)
        print(f'Vida do {jogador.nome}:')
        print(f'Defesa: {jogador.defesa_atual}/{jogador.defesa_max}')
        print(f"Vida: {jogador.vida_atual}/{jogador.vida_max}")
        print('-'*50)
        print(f'Vida do {inimigo.nome}:')
        print(f'{inimigo.vida_atual}/{inimigo.vida_max}')
        print('='*50)
        time.sleep(1)
        print("--- Sua ação ---\n")
        print(f"1 - Atacar com {jogador.item_equipado.nome if jogador.item_equipado else 'Mão'}")
        print("2 - Ver inventário")
        print("3 - Fugir")
        print('\n'*2)

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            jogador.ataque_basico(inimigo)
        elif escolha == "2":
            inventario(jogador, carro)
            continue
        elif escolha == "3":
            if randint(0,1) == 1:
                print(f"\n{jogador.nome} conseguiu fugir!")
                return False
            print(f"\n Não conseguiu fugir!")
        else:
            print("Opção inválida!")
            continue

        if not inimigo.esta_vivo():
            print(f"\n{inimigo.nome} foi derrotado!")
            time.sleep(1)
            return True

        inimigo.ataque_basico(jogador)

        if not jogador.esta_vivo():
            print(f"\n💀 {jogador.nome} foi derrotado!")
            return False

        

loot_edificios = {

    "Casa abandonada": [
        "Comida",
        "Agua",
        "Gasolina",
        'Etanol',
        "Pistola",
        'Colete'
    ],

    "Posto de gasolina": [
        "Gasolina",
        "Diesel",
        "Etanol",
        'Pneu',
        "Oleo"
    ],

    "Oficina mecânica": [
        "Caixa de Motor",
        "Pneu",
        'Oleo',
        'Chave inglesa',
        "Diesel"
    ],

    "Hospital": [
        "Kit medico",
        "Comida",
        "Agua",
        'Colete'
    ],

    "Delegacia": [
        "Pistola",
        "Espingarda",
        "Colete",
        "Kit medico"
    ],

    "Supermercado": [
        "Comida",
        "Agua",
        "Oleo",
        "Pneu"
    ],

    "Galpão industrial": [
        "Diesel",
        "Caixa de Motor",
        "Pneu",
    ],

    "Hotel abandonado": [
        "Comida",
        "Agua",
        "Kit medico",
        "Pistola"
    ],

    "Outpost": [
        "Caixa de Motor",
        "Diesel",
        "Pneu",
        "Colete",
        'Rifle'
    ]
    }
class Edificio:
    def __init__(self, nome, distancia, chance):
        self.nome = nome
        self.distancia = distancia
        self.chance_proporcional = chance

    def entrar(self,jogador, carro):
        loot = loot_edificios.get(self.nome, [])

        if loot:
            quantidade = randint(0, min(5, len(loot)))
            if quantidade> 0:
                itens_encontrados = random.sample(loot,quantidade)

                print("\nVocê encontrou:")
                for item_nome in itens_encontrados:
                    print('\n'*7)
                    print('-'*50)
                    print(f"  • {item_nome}")
                    print('-'*50)
                    print('\n'*7)
                    time.sleep(1)

                    if item_nome == 'Pistola':
                        novo_item = Item('Pistola',15,25,6,12)
                    elif item_nome == 'Espingarda':
                        novo_item = Item('Espingarda',30,60,4,8)
                    elif item_nome == 'Rifle':
                        novo_item = Item('Rifle',80,100,20,40)
                    elif item_nome == 'Chave inglesa':
                        novo_item = Item('Chave inglesa',5,10,5,10)
                    else:
                        novo_item = Item(item_nome,0,0,1,1)
                    jogador.inventario.adicionar(novo_item)
                    time.sleep(0.5)

            else:
                print('Tem NADA aqui ')
                print("\nSobrou nada pro Beta")
                print('\n'*7)
                time.sleep(2)
        # Procurar zumbis
        quantidade_zumbis = self.encontrar_zumbis()

        if quantidade_zumbis > 0:

            for i in range(quantidade_zumbis):

                zumbi = Inimigo(
                    "Zumbi",
                    randint(75, 100),
                    randint(25,50)
                )

                resultado = combate(jogador, zumbi, carro)

                if not resultado:
                    print("\n Você fugiu de medo")
                    time.sleep(1)
                    return
        print('.'*50)
        print("\nLocal explorado com sucesso!")
        print('.'*50)
        print('\n'*5)
        time.sleep(1)
        

    def encontrar_zumbis(self):

        chance = randint(1, 100)

        if  chance <= 50:

            quantidade = randint(1, 5)
            print('\n'*7)
            print('-'*50)
            print(f'Você encontrou {quantidade} zumbi(s)!')
            print('-'*50)
            print('\n'*7)
            time.sleep(2)
            return quantidade
        
        print('-'*50)
        print("\nNenhum zumbi encontrado")
        print('\n'*5)
        time.sleep(3)

        return 0

distancia_ultimo_edificio = 0

def verificar_edificio(carro, jogador):

    global distancia_ultimo_edificio

    if carro.distancia_percorrida < 1:
        return

    distancia_desde_ultimo = (
        carro.distancia_percorrida - distancia_ultimo_edificio)

    if distancia_desde_ultimo < 1:
        return

    if randint(1, 100) <= 50:
        edificios_disponiveis = [ed for ed in Edificios if carro.distancia_percorrida >= ed.distancia]
        if not edificios_disponiveis:
            return

    
        pesos = [edificio.chance_proporcional for edificio in edificios_disponiveis]
        edificio = random.choices(edificios_disponiveis, weights=pesos,k=1)[0]

        distancia_ultimo_edificio = carro.distancia_percorrida

        print("=" * 50)
        print(f"{edificio.nome.upper()} AVISTADO!")
        print("=" * 50)

        while True:

            print("\n1 - Explorar")
            print("2 - Continuar viagem")
            print('\n'*8)

            escolha = input("\nEscolha: ").strip()

            if escolha == "1":
                edificio.entrar(jogador,carro)
                break

            elif escolha == "2":
                print("\ncontinuando a viagem.")
                time.sleep(1)
                break

            else:
                print("\nOpção inválida.")
                time.sleep(2)
Edificios = [
    # Nome (str), Distancia (int), Chance (int)
    Edificio("Casa abandonada", 1, 40),
    Edificio("Posto de gasolina", 1, 30),
    Edificio("Oficina mecânica", 1, 25),
    Edificio("Hospital", 1, 25),
    Edificio("Delegacia", 1,20),
    Edificio("Supermercado", 1, 30),
    Edificio("Galpão industrial", 1, 15),
    Edificio("Hotel abandonado", 1, 25),
    Edificio("Outpost", 1, 10)
]

#INICIO DO JOGO

nome_da_lenda = input('Escolha Seu nome sobrevivente: ')
print(f'\nBoa sorte... {nome_da_lenda}\n')

jogador = Jogador(nome_da_lenda)

carro = Carro('v3_aspirado|motor_hibrido(Motor de KWID)',jogador)

time.sleep(3)
print('Iniciando')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
print('='*50)
time.sleep(2)
print('o Vírus se expalhou...\n')
time.sleep(3)
print('mais de 90%','da população viraram zumbis...\n')
time.sleep(5)
print('como a ultima experança da resistência humana...\n')
time.sleep(5)
print('Sua missão é cruzar a fronteira á 200km de distância, em busca da cura.\n')
time.sleep(5)
print('dando partida no carro..')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('\n'*7)
print('='*50)
print('---The Long Road---')
print('='*50)
print('\n'*7)
time.sleep(5)
while True:
    print('='*50)
    print(f" Destino Final: {carro.distancia_percorrida}/200 km")
    print('-.'*25)
    print(f"Agua: {carro.agua_atual}/{carro.agua_max}L | Óleo: {carro.oleo_atual}/{carro.oleo_max}L" )
    print(f"Gasolina: {carro.tanques['Gasolina']} - Etanol: {carro.tanques['Etanol']} - Diesel: {carro.tanques['Diesel']}")     
    print(f"Pneu: {carro.pneu_vida}%")
    print('-'*50)
    print(f'Proteção: {jogador.defesa_atual}/{jogador.defesa_max}')
    print(f"   Saúde: {jogador.vida_atual}/{jogador.vida_max}")
    print('-'*50)
    print(f" Motor: {carro.motor}")
    print("=" * 50)

    print("1 - Dirigir")
    print("2 - Inventário")
    print("3 - Status")
    print("4 - Sair")

    escolha = input("Escolha: ").strip()

    if escolha == "1":

        terminou = carro.mover()

        if terminou:
            break
        verificar_edificio(carro, jogador)
            
            
    elif escolha == "2":
        inventario(jogador, carro)

    elif escolha == "3":
        jogador.status()

    elif escolha == "4":
        print(f"\n{nome_da_lenda} abortou a missão")
        time.sleep(3)
        print('='*50)
        print('todo mundo morreu')
        print("="*50)
        break

    else:
        print("\n Opção inválida.")
        time.sleep(2)