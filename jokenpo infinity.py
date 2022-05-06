# Jókenpô
from time import sleep
from random import randint

def espaço():
    print('=' * 60)

espaço()
print('{:^60}'.format(' Jókenpô '))
espaço()
print('Jó..', end='')
sleep(0.5)
print('ken..', end='')
sleep(0.5)
print('pô!')
sleep(0.5)

print('{:=^60}'.format(' Até Parar '))


def jogo():
    vit = 0
    der = 0
    emp = 0
    i = False
    while i == False:
        escolha = int(input('Escolha uma das opções: [1] ▲ PEDRA | [2] ▬ PAPEL | [3] ♣ TESOURA | [0] Sair\n-> '))
        while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 0: # VALIDAÇÃO
            escolha = int(input('-> '))
        computador = randint(1, 3)

        if escolha == 1 and computador == 1:
            print('▲ PEDRA X ▲ PEDRA \nEmpatou :)')
            emp = emp + 1
        elif escolha == 1 and computador == 2:
            print('▲ PEDRA X ▬ PAPEL \nVocê perdeu :(')
            der = der + 1
        elif escolha == 1 and computador == 3:
            print('▲ PEDRA X ♣ TESOURA \nVocê ganhou ;)')
            vit = vit + 1

        elif escolha == 2 and computador == 1:
            print('▬ PAPEL X ▲ PEDRA \nVocê ganhou ;)')
            vit = vit + 1
        elif escolha == 2 and computador == 2:
            print('▬ PAPEL X ▬ PAPEL \nEmpatou :)')
            emp = emp + 1
        elif escolha == 2 and computador == 3:
            print('▬ PAPEL X ♣ TESOURA \nVocê perdeu :(')
            der = der + 1

        elif escolha == 3 and computador == 1:
            print('♣ TESOURA X ▲ PEDRA \nVocê perdeu :(')
            der = der + 1
        elif escolha == 3 and computador == 2:
            print('♣ TESOURA X ▬ PAPEL \nVocê ganhou ;)')
            vit = vit + 1
        elif escolha == 3 and computador == 3:
            print('♣ TESOURA X ♣ TESOURA \nEmpatou :)')
            emp = emp + 1

        elif escolha == 0:
            print('Fim de Jogo')
            i = True

        espaço()
        sleep(1)

    print(f'Vitórias: {vit} | Derrotas: {der} | Empates: {emp}')
    if vit > der:
        print('Você ganhou a partida!!')
    elif der > vit:
        print('Você perdeu a partida :(')
    else:
        print('Empatou x.x')
    print('\n')

while True:
    jogo()
    escolha = int(input("Jogar de novo? [1] Sim [2] Não\n->"))
    while escolha != 1 and escolha != 2:
        escolha = int(input("->"))
    if escolha == 2:
        break
    espaço()
