#JOGO EXPLORACAO MASMORRA
#Alunos: Gustavo Belançon Mendes - Hector Dorrighello Giacon

import random
import time
from colorama import init, Fore, Back

#MONSTROS:
#->Dragão: 12hp, 50% de reducao de dano magico
class Dragon:
	def __init__(self):
		self.hp = 12
		self.reducao = "magico"
		self.porc_reducao = 0.5

#->Orc: 6hp, 50% reducao de dano fisico
class Orc:
	def __init__(self):
		self.hp = 6
		self.reducao = "fisico"
		self.porc_reducao = 0.5

#->Undead: 8hp, 50% reducao de dano veneno
class Undead:
	def __init__(self):
		self.hp = 8
		self.reducao = "veneno"
		self.porc_reducao = 0.5

class Monstro:
	def __init__(self, classe, reducao, porc_reducao, hp):
		self.classe = classe
		self.reducao = reducao
		self.porc_reducao = porc_reducao
		self.hp = hp

#AVENTUREIROS:
#->Druid: acerta os 3 primeiros monstros com 5 de dano veneno
class Druid:
	def __init__(self):
		self.dano = 5
		self.tipo_dano = "veneno"

#->Mage: acerta os 4 primeiros monstros com 4 de dano magico
class Mage:
	def __init__(self):
		self.dano = 4
		self.tipo_dano = "magico"

#->Warrior: acerta os 2 primeiros monstros com 6 de dano fisico
class Warrior:
	def __init__(self):
		self.dano = 6
		self.tipo_dano = "fisico"

class Aventureiro:
	def __init__(self, classe, dano, tipo_dano):
		self.classe = classe
		self.dano = dano
		self.tipo_dano = tipo_dano

#O JOGO:
	#inicialmente escolher a dificuldade do jogo
	#definir a dificuldade com base no numero de aventureiros da equipe
	#o número de monstros para cada nível é: valor do nível + 3 monstros
	#monstros organizados em uma fila sorteada de maneira aleatória
	#a cada rodada o jogador irá selecionar o tipo de aventureiro que irá atacar
	#um aventureiro so pode realizar uma acao por masmorra, dps ele sai do grupo
	#o jogo acaba quando nao existirem mais aventureiros para atacar

def gerar_monstros(lvl):
	qnt = lvl + 3
	cont = qnt
	monstros = []

	while cont > 0:
		index = random.randint(1,3)

		if index == 1:
			drag = Dragon()
			monster = Monstro("drag", drag.reducao, drag.porc_reducao, drag.hp)
			monstros.append(monster)

		elif index == 2:
			orc = Orc()
			monster = Monstro("orc", orc.reducao, orc.porc_reducao, orc.hp)
			monstros.append(monster)

		else:
			und = Undead()
			monster = Monstro("undead", und.reducao, und.porc_reducao, und.hp)
			monstros.append(monster)

		cont -= 1

	return monstros

def print_monstros(monstros, flag):
	if flag == 1:
		for monstro in monstros:
			print("\t" + monstro.classe+" //" + Back.WHITE + Fore.RED + " Redução contra "+monstro.reducao + Back.RESET + Fore.RESET +" //" + Back.RED + Fore.WHITE + " HP: "+str(monstro.hp) + Back.RESET + Fore.RESET)
	else:
		for monstro in monstros:
			print(monstro.classe+" //" + Back.WHITE + Fore.RED + " Redução contra " + monstro.reducao + Back.RESET + Fore.RESET +" //" + Back.RED + Fore.WHITE + " HP: "+str(monstro.hp) + Back.RESET + Fore.RESET)
	print()

def print_aventureiros(aventureiros, flag):
	cont_druida = 0
	cont_mage = 0
	cont_warrior = 0
	for avent in aventureiros:
		if avent.classe == "druid":
			cont_druida += 1
		elif avent.classe == "mage":
			cont_mage += 1
		else:
			cont_warrior += 1
	if flag == 1:
		print("\tdruid //" + Back.RED + Fore.WHITE + " Dano: 5" + Back.RESET + Fore.RESET + " //" + Back.WHITE + Fore.RED + " Elemento: veneno" + Back.RESET + Fore.RESET + " //" + Back.RED + Fore.WHITE + " quantidade: " + str(cont_druida) + Back.RESET + Fore.RESET)
		print("\tmage //" + Back.RED + Fore.WHITE + " Dano: 4" + Back.RESET + Fore.RESET + " //" + Back.WHITE + Fore.RED + " Elemento: magico" + Back.RESET + Fore.RESET + " //" + Back.RED + Fore.WHITE + " quantidade: " + str(cont_mage) + Back.RESET + Fore.RESET)
		print("\twarrior //" + Back.RED + Fore.WHITE + " Dano: 6" + Back.RESET + Fore.RESET + " //" + Back.WHITE + Fore.RED + " Elemento: fisico" + Back.RESET + Fore.RESET + " //" + Back.RED + Fore.WHITE + " quantidade: " + str(cont_warrior) + Back.RESET + Fore.RESET)	
	else:
		print("druid //" + Back.RED + Fore.WHITE + " Dano: 5" + Back.RESET + Fore.RESET + " //" + Back.WHITE + Fore.RED + " Elemento: veneno" + Back.RESET + Fore.RESET + " //" + Back.RED + Fore.WHITE + " quantidade: " + str(cont_druida) + Back.RESET + Fore.RESET)
		print("mage //" + Back.RED + Fore.WHITE + " Dano: 4" + Back.RESET + Fore.RESET + " //" + Back.WHITE + Fore.RED + " Elemento: magico" + Back.RESET + Fore.RESET + " //" + Back.RED + Fore.WHITE + " quantidade: " + str(cont_mage) + Back.RESET + Fore.RESET)
		print("warrior //" + Back.RED + Fore.WHITE + " Dano: 6" + Back.RESET + Fore.RESET + " //" + Back.WHITE + Fore.RED + " Elemento: fisico" + Back.RESET + Fore.RESET + " //" + Back.RED + Fore.WHITE + " quantidade: " + str(cont_warrior) + Back.RESET + Fore.RESET)	
	print()

def atk_warrior(aventureiros, monstros):
	for avent in aventureiros:
		if avent.classe == "warrior":
			if len(monstros) >= 1:
				if avent.tipo_dano == monstros[0].reducao:
					monstros[0].hp = monstros[0].hp - (avent.dano * monstros[0].porc_reducao)
				else:
					monstros[0].hp = monstros[0].hp - avent.dano

				if len(monstros) >= 2:

					if avent.tipo_dano == monstros[1].reducao:
						monstros[1].hp = monstros[1].hp - (avent.dano * monstros[1].porc_reducao)
					else:
						monstros[1].hp = monstros[1].hp - avent.dano

					if monstros[1].hp <= 0:
						del monstros[1]
					if monstros[0].hp <= 0:
						del monstros[0]

				else:
					if monstros[0].hp <= 0:
						del monstros[0]

			aventureiros.remove(avent)
			return aventureiros, monstros

	print("\nVocê não possui mais guerreiros na sua equipe, escolha outra classe para atacar!\n")
	return aventureiros, monstros

def atk_druid(aventureiros, monstros):
	for avent in aventureiros:
		if avent.classe == "druid":
			if len(monstros) >= 1:
				if avent.tipo_dano == monstros[0].reducao:
					monstros[0].hp = monstros[0].hp - (avent.dano * monstros[0].porc_reducao)
				else:
					monstros[0].hp = monstros[0].hp - avent.dano

				if len(monstros) >= 2:

					if avent.tipo_dano == monstros[1].reducao:
						monstros[1].hp = monstros[1].hp - (avent.dano * monstros[1].porc_reducao)
					else:
						monstros[1].hp = monstros[1].hp - avent.dano

					if len(monstros) >= 3:
						if avent.tipo_dano == monstros[2].reducao:
							monstros[2].hp = monstros[2].hp - (avent.dano * monstros[2].porc_reducao)
						else:
							monstros[2].hp = monstros[2].hp - avent.dano

						if monstros[2].hp <= 0:
							del monstros[2]
						if monstros[1].hp <= 0:
							del monstros[1]
						if monstros[0].hp <= 0:
							del monstros[0]
					else:
						if monstros[1].hp <= 0:
							del monstros[1]
						if monstros[0].hp <= 0:
							del monstros[0]

				else:
					if monstros[0].hp <= 0:
						del monstros[0]

			aventureiros.remove(avent)
			return aventureiros, monstros

	print("\nVocê não possui mais druids na sua equipe, escolha outra classe para atacar!\n")
	return aventureiros, monstros

def atk_mage(aventureiros, monstros):
	for avent in aventureiros:
		if avent.classe == "mage":
			if len(monstros) >= 1:
				if avent.tipo_dano == monstros[0].reducao:
					monstros[0].hp = monstros[0].hp - (avent.dano * monstros[0].porc_reducao)
				else:
					monstros[0].hp = monstros[0].hp - avent.dano

				if len(monstros) >= 2:
					if avent.tipo_dano == monstros[1].reducao:
						monstros[1].hp = monstros[1].hp - (avent.dano * monstros[1].porc_reducao)
					else:
						monstros[1].hp = monstros[1].hp - avent.dano

					if len(monstros) >= 3:

						if avent.tipo_dano == monstros[2].reducao:
							monstros[2].hp = monstros[2].hp - (avent.dano * monstros[2].porc_reducao)
						else:
							monstros[2].hp = monstros[2].hp - avent.dano

						if len(monstros) >= 4:

							if avent.tipo_dano == monstros[3].reducao:
								monstros[3].hp = monstros[3].hp - (avent.dano * monstros[3].porc_reducao)
							else:
								monstros[3].hp = monstros[3].hp - avent.dano

							if monstros[3].hp <= 0:
								del monstros[3]
							if monstros[2].hp <= 0:
								del monstros[2]
							if monstros[1].hp <= 0:
								del monstros[1]
							if monstros[0].hp <= 0:
								del monstros[0]

						else:

							if monstros[2].hp <= 0:
								del monstros[2]
							if monstros[1].hp <= 0:
								del monstros[1]
							if monstros[0].hp <= 0:
								del monstros[0]

					else:
						if monstros[1].hp <= 0:
							del monstros[1]
						if monstros[0].hp <= 0:
							del monstros[0]

				else:
					if monstros[0].hp <= 0:
						del monstros[0]

			aventureiros.remove(avent)
			return aventureiros, monstros

	print("\nVocê não possui mais mages na sua equipe, escolha outra classe para atacar!\n")
	return aventureiros, monstros

def rounds(aventureiros, monstros, cont_level):
	cont_round = 1
	while len(aventureiros) > 0 and len(monstros) > 0:
		print("\n+------------------------------------------------------------------+")
		print("\t\t" + Back.WHITE + Fore.RED + "* LEVEL " +str(cont_level) + " - ROUND " + str(cont_round) + " *\n" + Back.RESET + Fore.RESET)
		print_monstros(monstros,1)
		print_aventureiros(aventureiros,1)
		avent_atk = input("Qual aventureiro irá atacar? <d>Druid, <m>Mago ou <w>Guerreiro? ")
		print("+------------------------------------------------------------------+\n")

		if avent_atk == "w":
			aventureiros, monstros = atk_warrior(aventureiros, monstros)
		if avent_atk == "d":
			aventureiros, monstros = atk_druid(aventureiros, monstros)
		if avent_atk == "m":
			aventureiros, monstros = atk_mage(aventureiros, monstros)
		cont_round += 1

	return aventureiros


def jogo():

	print("Monte sua equipe para derrotar os monstros da masmorra!\n")
	print("\tSelecione a dificuldade:")
	print("\t" + Back.BLUE + Fore.WHITE + "<1>Fácil 	(30 aventureiros)" + Back.RESET)
	print("\t" + Back.YELLOW + Fore.WHITE + "<2>Médio 	(18 aventureiros)" + Back.RESET)
	print("\t" + Back.RED + Fore.WHITE + "<3>Difícil 	(09 aventureiros)" + Back.RESET)
	print("\t" + Back.WHITE + Fore.RED + "<4>Sair do jogo =(" + Back.RESET, Fore.RESET)

	dif = int(input("\nEscolha entre as dificuldades 1, 2 ou 3:\n> "))
	num_aventureiros = 18

	if dif == 1:
		print(Back.WHITE + Fore.RED + "Dificuldade fácil escolhida!\n" + Back.RESET)
		num_aventureiros = 30
	elif dif == 2:
		print(Back.WHITE + Fore.RED + "Dificuldade média escolhida!\n" + Back.RESET)
		num_aventureiros = 18
	elif dif == 3:
		print(Back.WHITE + Fore.RED + "Dificuldade difícil escolhida!\n" + Back.RESET)
		num_aventureiros = 9
	elif dif == 4:
		exit()
	else:
		print(Back.WHITE + Fore.RED + "Você irá jogar com a dificuldade padrão (Médio)\n\n" + Back.RESET)

	aventureiros = []
	flag = 0

	print(Back.WHITE + Fore.RED + '\nA seguir você irá escolher a quantidade de aventureiros para cada classe.')
	print('- Os druids causam 5 de dano veneno por ataque e acertam os 3 primeiros inimigos.')
	print('- Já os mages possuem 4 de dano mágico, acertando 4 inimigos na linha de frente da batalha.')
	print('- Os guerreiros dão 6 de dano físico nos 2 primeiros inimigos com seu ataque.\n\n' + Back.RESET + Fore.RESET)
	time.sleep(2)

	while flag == 0:
		n_druids = int(input("Escolha a quantidade de druids da sua equipe: "))
		if (num_aventureiros - n_druids) >= 0:
			flag = 1
			num_aventureiros = num_aventureiros - n_druids
			print("Você adicionou " + Back.WHITE + Fore.RED + str(n_druids) + " druids!" + Back.RESET + Fore.RESET)
			while n_druids > 0:
				druid = Druid()
				avent = Aventureiro("druid", druid.dano, druid.tipo_dano)
				aventureiros.append(avent)
				n_druids -= 1
		else:
			print("Quantidade de druids selecionada é maior do que o seu número de aventureiros!\nDigite uma quantidade menor.")
	
	print("Ainda restam " + Back.WHITE + Fore.RED + str(num_aventureiros) + Back.RESET + Fore.RESET + " aventureiros para adicionar à sua equipe!")
	flag = 0

	time.sleep(1)

	while flag == 0:
		n_mages = int(input("\nEscolha a quantidade de mage da sua equipe: "))
		if (num_aventureiros - n_mages) >= 0:
			flag = 1
			num_aventureiros = num_aventureiros - n_mages
			print("Você adicionou " + Back.WHITE + Fore.RED + str(n_mages) + " mages!" + Back.RESET + Fore.RESET)
			while n_mages > 0:
				mage = Mage()
				avent = Aventureiro("mage", mage.dano, mage.tipo_dano)
				aventureiros.append(avent)
				n_mages -= 1
		else:
			print("Quantidade de mages selecionada é maior do que o seu número de aventureiros!\nDigite uma quantidade menor.")
	
	print("Ainda restam " + Back.WHITE + Fore.RED + str(num_aventureiros) + Back.RESET + Fore.RESET + " aventureiros para adicionar à sua equipe!")
	flag = 0

	time.sleep(1)

	while flag == 0:
		n_warrior = int(input("\nEscolha a quantidade de guerreiros da sua equipe: "))
		if (num_aventureiros - n_warrior) >= 0:
			flag = 1
			num_aventureiros = num_aventureiros - n_warrior
			print("Você adicionou " + Back.WHITE + Fore.RED + str(n_warrior) + " guerreiros!")
			while n_warrior > 0:
				warrior = Warrior()
				avent = Aventureiro("warrior", warrior.dano, warrior.tipo_dano)
				aventureiros.append(avent)
				n_warrior -= 1
		else:
			print("Quantidade de guerreiros selecionada é maior do que o seu número de aventureiros!\nDigite uma quantidade menor.")

	print("\n\nEquipe pronta!\n" + Back.RESET + Fore.RESET + "Você tem " + Back.WHITE + Fore.RED + str(len(aventureiros)) + Back.RESET + Fore.RESET + " aventureiros na sua equipe.")
	print_aventureiros(aventureiros,0)

	time.sleep(1)

	#iniciar a partida com a fila de monstros aleatórios pro level 1
	monstros = []
	lvl = 0

	print(Back.WHITE + Fore.RED + "O jogo irá começar!")
	print("Em cada round escolha o aventureiro que irá atacar digitando 'd' para druid, 'm' para mago e 'w' para guerreiro.")
	print("Cada aventureiro que atacar irá imediatamente sair da sua equipe.")
	print("Voce avança de nível ao acabar com todos os inimigos.\nPorém se voce ficar sem aventureiros em sua equipe, é fim de jogo.")
	print("\nBoa sorte!\n" + Back.RESET + Fore.RESET)

	time.sleep(2)

	while len(aventureiros) > 0:
		lvl += 1
		monstros = gerar_monstros(lvl)
		aventureiros = rounds(aventureiros, monstros, lvl)
		

	print("Fim de jogo!")
	print("Voce chegou até o nível " + str(lvl))
	time.sleep(2)

def main():
	init()
	print(Back.GREEN + Fore.WHITE + "\n/*/*/*/* JOGO DE EXPLORACAO DA MASMORRA */*/*/*/" + Back.RESET + Fore.RESET)
	jogo()
	

main()
