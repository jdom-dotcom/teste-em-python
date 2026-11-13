
import time #time pra melhor experiencia
import random #random caso o caixa ficar sem celula
import os #limpar terminal

print('='*50)
print('Simulador de Caixa (Eletrônico)')#titulo padrão
print('='*50,'\n')
#variaveisssss


saldo = 0
dinheiro_na_mão = 1000

ultimo_saque = 0
ultimo_deposito = 0


while True:
        
#simulção de criação de conta

        print('---> Criação da Conta <---\n')
        print('[Digite o nome da sua nova conta]')
        nome =  input('\nNome: ').replace(' ','')
        print('='*50)
        print('\n[Crie uma senha]\n')
        print('-'*50)
        print('-> apenas números')
        print('-> com 6 digitos')
        print('-'*50)
        senha = input('Senha: ').replace('','')
        print('='*50)

        tamanho_ok = len(senha) == 6 #senha só será aceita se tiver 6 numeros apenas
        apenas_numeros = senha.isdigit() #verifica se tudo é numero

        if apenas_numeros and tamanho_ok: #se os d 2 for verdeiro (1 and 1)= true, a conta é criada
            print('\n'*7)
            print('-'*50)
            print('Conta criada com sucesso!')
            print('-'*50)
            print('\n'*7)
            time.sleep(2)
            os.system('cls')
            break

        else:#caso contrário devera inserir os valores novamente
            print('\n'*7)
            print('-'*55)
            print('Erro! a senha tem que ter (6) digitos')
            print('-'*55)
            print('\n'*7)
            time.sleep(2)
            print('e apenas [números]')
            time.sleep(3)
            print('\n'*7)
            print('='*50)
            os.system('cls')
#encerrando o while da senha voce cai direto no painel de entrada do caixa eletrônico
tentativa = 0 
quantidade_de_tempo_de_espera = 0
while True:
#essas váriaveis verificarão se a senha e o usurio criado antes estão certa
    desbloqueio = False

    print('='*50)
    print('---- Caixa Eletrônico ----\n')
    print('---> ENTRAR <---')
    print('='*50)
    nome_caixa = input('Insira nome: ')
    print('-'*50)
    senha_caixa = input('Insira a Senha: ')
    print('='*50)
    #aqui é a conversão para true | repare que usei d 2 if novamente porque os tem que está ativiado ao mesmo tempo para desbloquear
    if nome_caixa == nome and senha_caixa == senha:
        desbloqueio = True

    else:#caso usuario erre aparecerá essa mensagem
        print('\n'*7)
        print('-'*50)
        print('[Nome] ou [senha] estão invalidos')
        print('-'*50)
        print('\n'*7)
        time.sleep(1.5)
        os.system('cls')
        tentativa += 1

        if tentativa == 3:

            tentativa = 0 
            quantidade_de_tempo_de_espera += 1
            valor_tempo_espera = (15 * quantidade_de_tempo_de_espera)

            for i in range(valor_tempo_espera,0,-1):
                print('\n'*7)
                print('='*30)
                print('      > Caixa Bloqueado <      ')
                print(f'    --------[{i}]-------')
                print('='*30,'\n'*7)
                time.sleep(1)
                os.system('cls')
                if valor_tempo_espera == 120:
                    quantidade_de_tempo_de_espera = 1

    #se acertar ele vai direto para sua conta no banco
    if desbloqueio:

        os.system('cls')
        
        while True: # esse é o segundo while | 1 while (ENTRAR) para entrar com a senha e nome, esse não quebra. E o 2º While para entrar na sua conta, esse já quebra se ele apertar em sair, voltando para inicial
            print('='*50)
            print('---- Caixa Eletrônico ----\n')# menu principal mostrando as opção
            print('---> Menu <---')
            print(f'Conta [{nome}]')
            print('='*50)
            print('--- Opções ---\n')
            print('1- Consultar saldo')
            print('2- Sacar')
            print('3- Depositar')
            print('4- Sair')
            print('.'*50)
            escolha = input('Escolha: ')#entrada da escolha
#CADA ESCOLHA 1 AO 3 TEM 1 while |isso serve para evitar do codigo quebrar ou ficar retornando no inicio a cada erro
            if escolha == '1':
                os.system('cls')
                while True: #saldo da conta com ultimo saque e deposito
                    print('='*50)
                    print('--- Caixa Eletrônico ---\n')
                    print('---> Extrato <---\n')
                    print('-'*50)
                    print(f'Saldo: [R$ {saldo}]')
                    print('-'*50)
                    print(f'\nUltimo Deposito: (R$ {ultimo_deposito}) | Último Saque: (R$ {ultimo_saque})')
                    print('='*50)
                    print(f'Dinheiro na mão: (R$ {dinheiro_na_mão})')
                    voltar = input('\nPressione [Enter] pra voltar ')

                    if voltar == '':
                        os.system('cls')
                        break
                    else:
                      os.system('cls')  

            elif escolha == '2':
                os.system('cls')
                voltar_escolha_2 = False
                while True:
                    saque = 0
                    tem_cedula = random.randint(1,100) #verificação se tem cedula
                    try:#caso tenta quebrar com letras
                        print('='*50)
                        print('--- Caixa Eletrônico ---\n')  
                        print('---> Operção: [Sacar] <---\n')#menu principal básico
                        print('-'*50)
                        print('Digite o Valor do Saque')
                        print('='*50,'\n')
                        saque = int(input('Valor R$: '))#entrada do valor
                        

                    except ValueError:#retorno do erro
                        print('\n'*9)
                        print('-'*50)
                        print('[apenas numeros]')
                        print('-'*50)
                        print('\n'*5)
                        time.sleep(1)
                        print('Insira o Valor Novamente..')
                        time.sleep(2)
                        os.system('cls')
                        continue

                    if saque > saldo: #se o saldo não for suficiente
                        print('\n'*7)
                        print('-'*50)
                        print('Saldo Insuficiente')# retorno do motivo
                        print('-'*50)
                        print('\n'*7)
                        time.sleep(2)
                        os.system('cls')
                        break #a variavel fica verdadeira

                    elif tem_cedula <= 10: #se o caixa fica sem cedula | caso o numero sorteado sejá 0 á 10 = 10%
                        print('\n'*7)
                        print('-'*50)
                        print('[Caixa sem Cedula]') #retorno do motivo 2
                        print('-'*50)
                        print('\n'*5)
                        time.sleep(1)
                        print('(Tente Novamente Mais Tarde)')
                        time.sleep(2)
                        os.system('cls')
                        break

                    else:#se as duas opçao passar
                        saldo = saldo - saque #operção
                        dinheiro_na_mão = dinheiro_na_mão + saque  
                        ultimo_saque = saque
                                           
                        while True:# novo while caso queira fazer um novo saque sem precisar voltar ao menu
                            os.system('cls')
                            print('-----> [Saque Realizado] <-----\n')
                            print('='*50)
                            print(f'Você Sacou: [R$ {saque}]')#quanto você sacou
                            print('.'*50)
                            print(f'Saldo Restante: [R$ {saldo}]')#restante
                            print('='*50,'\n')
                            print('-'*50)
                            time.sleep(2)
                            print('Realizar novo saque?')
                            print(' 1- sim | 2- não')
                            resposta_do_saque = input('Escolha: ')

                            if resposta_do_saque == '1': #se a entrada da resposta for 1 quebra e realiza 
                                os.system('cls')
                                break

                            elif resposta_do_saque == '2': #se entrada for 2 quebra e ativa o voltar
                                os.system('cls')
                                voltar_escolha_2 = True
                                break

                            else:
                                print('\n'*7)
                                print('-'*50)
                                print('Valor Indevido')# caso ao contrário 
                                print('-'*50)
                                print('\n'*5)
                                time.sleep(1)
                                print('Apenas [1] ou [2]')
                                time.sleep(2)
                                os.system('cls')


                    if voltar_escolha_2: #se a resposta do saque for 2 loop quebra e volta para menu
                        os.system('cls')
                        break

            elif escolha == '3':
                os.system('cls')
                voltar_escolha_3 = False
                while True:
                    deposito = 0
                    try:#novamente caso tente quebrar
                        print('='*50)
                        print('--- Caixa Eletrônico ---\n')
                        print('---> Operação [Depósito] <---\n')#menu padrão
                        print('-'*50)
                        print('Digite Valor do Depósito')
                        print('-'*50,'\n')
                        print('='*50)
                        deposito = int(input('Valor R$: '))

                    except ValueError:
                        print('\n'*9)
                        print('-'*50)
                        print('[apenas numeros]')#retorno do erro
                        print('-'*50)
                        print('\n'*7)
                        time.sleep(1)
                        print('Insira o Valor Novamente..')
                        time.sleep(2)
                        os.system('cls')
                        continue

                    if deposito > dinheiro_na_mão:
                        print('\n'*7)
                        print('-'*50)
                        print('Dinheiro Insuficiente!!')# retorno do motivo
                        print('-'*50)
                        print('\n'*7)
                        time.sleep(2)
                        break
                        os.system('cls')
                    else:
                        
                        dinheiro_na_mão = dinheiro_na_mão - deposito
                        saldo = saldo + deposito #operação 
                        ultimo_deposito = deposito
                        
                    #se passar ali em cima cai em um outro loop
                        while True:
                            os.system('cls')
                            print('-----> [Depósito Realizado] <----- ','\n')
                            print('='*50)
                            print(f'Você Depositou: [R$ {deposito}]')#nesse loop mostra o valor do deposito e do saldo, e ainda pergunta se quer realizar um novo deposito
                            print('.'*50)
                            print(f'Saldo Restante: [R$ {saldo}]')
                            print('='*50,'\n')
                            print('-'*50)
                            time.sleep(2)
                            print('Realizar novo depósito?')
                            print(' 1- sim | 2- não')
                            resposta_do_deposito = input('Escolha: ')

                            if resposta_do_deposito == '1':
                                os.system('cls')
                                break

                            elif resposta_do_deposito == '2':
                                os.system('cls')
                                voltar_escolha_3 = True
                                break
                            
                            else:#caso ao contrário...
                                print('\n'*7)
                                print('-'*50)
                                print('Valor Indevido')
                                print('-'*50)
                                print('\n'*5)
                                time.sleep(1)
                                print('Apenas [1] ou [2]')
                                time.sleep(2)
                                os.system('cls')

                    
                    if voltar_escolha_3:# se a resposta for 2 o loop encerra voltando para menu
                        os.system('cls')
                        break

            elif escolha == '4':
                print('\n'*7)
                print('-'*50)
                print('ENCERRANDO...')
                print('-'*50)
                print('\n'*7)
                time.sleep(2)
                os.system('cls')
                break
                #encerramento quebra o loop da conta e vai para o loop do entrar pedindo a senha e o usuario novamente
            else:
                print('\n'*7)
                print('-'*50)
                print('Valor Indevido')
                print('-'*50)
                print('\n'*5)
                time.sleep(1)
                print('Apenas [1]  [2]  [3] ou [4]')
                time.sleep(2)
                os.system('cls')# caso coloque algum valor indevido

#NOTA: o codigo foi 98% feito sozinho, só tive um erro nas operaçoes onde coloquei (saldo-saque) e (saldo+deposito) em vez de colocar (saldo = saque-deposito), um erro bobo que não percebi e acabai pedindo ajuda da IA nessa parte