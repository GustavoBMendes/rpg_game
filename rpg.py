#JOGO EXPLORACAO MASMORRA
#Alunos: Gustavo Belançon Mendes - Hector Dorrighello Giacon

import random

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

def print_monstros(monstros):
	for monstro in monstros:
		print(monstro.classe+" // Redução contra "+monstro.reducao+" // HP: "+str(monstro.hp))
	print()

def print_aventureiros(aventureiros):
	for avent in aventureiros:
		print(avent.classe+" // Dano: "+str(avent.dano)+" // Elemento: "+avent.tipo_dano)
	print()

def atk_warrior(aventureiros, monstros):
	for avent in aventureiros:
		if avent.classe == "warrior":
			if avent.tipo_dano == monstros[0].reducao:
				monstros[0].hp = monstros[0].hp - (avent.dano * monstros[0].porc_reducao)
			else:
				monstros[0].hp = monstros[0].hp - avent.dano

			if avent.tipo_dano == monstros[1].reducao:
				monstros[1].hp = monstros[1].hp - (avent.dano * monstros[1].porc_reducao)
			else:
				monstros[1].hp = monstros[1].hp - avent.dano

			if monstros[1].hp <= 0:
				del monstros[1]
			if monstros[0].hp <= 0:
				del monstros[0]

			aventureiros.remove(avent)
			return aventureiros, monstros

	print("\nVocê não possui mais guerreiros na sua equipe, escolha outra classe para atacar!\n")
	return aventureiros, monstros

def atk_druid(aventureiros, monstros):
	for avent in aventureiros:
		if avent.classe == "druid":
			if avent.tipo_dano == monstros[0].reducao:
				monstros[0].hp = monstros[0].hp - (avent.dano * monstros[0].porc_reducao)
			else:
				monstros[0].hp = monstros[0].hp - avent.dano

			if avent.tipo_dano == monstros[1].reducao:
				monstros[1].hp = monstros[1].hp - (avent.dano * monstros[1].porc_reducao)
			else:
				monstros[1].hp = monstros[1].hp - avent.dano

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

			aventureiros.remove(avent)
			return aventureiros, monstros

	print("\nVocê não possui mais druids na sua equipe, escolha outra classe para atacar!\n")
	return aventureiros, monstros

def atk_mage(aventureiros, monstros):
	for avent in aventureiros:
		if avent.classe == "mage":
			if avent.tipo_dano == monstros[0].reducao:
				monstros[0].hp = monstros[0].hp - (avent.dano * monstros[0].porc_reducao)
			else:
				monstros[0].hp = monstros[0].hp - avent.dano

			if avent.tipo_dano == monstros[1].reducao:
				monstros[1].hp = monstros[1].hp - (avent.dano * monstros[1].porc_reducao)
			else:
				monstros[1].hp = monstros[1].hp - avent.dano

			if avent.tipo_dano == monstros[2].reducao:
				monstros[2].hp = monstros[2].hp - (avent.dano * monstros[2].porc_reducao)
			else:
				monstros[2].hp = monstros[2].hp - avent.dano

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

			aventureiros.remove(avent)
			return aventureiros, monstros

	print("\nVocê não possui mais mages na sua equipe, escolha outra classe para atacar!\n")
	return aventureiros, monstros

def rounds(aventureiros, monstros):
	while len(aventureiros) > 0 or len(monstros) > 0:
		avent_atk = input("Qual aventureiro irá atacar? druid, mage ou warrior?")
		if avent_atk == "warrior":
			aventureiros, monstros = atk_warrior(aventureiros, monstros)
		if avent_atk == "druid":
			aventureiros, monstros = atk_druid(aventureiros, monstros)
		if avent_atk == "mage":
			aventureiros, monstros = atk_mage(aventureiros, monstros)

		print_monstros(monstros)
		print_aventureiros(aventureiros)

	return aventureiros


def jogo():

	print("Monte sua equipe para derrotar os monstros da masmorra!\n")
	print("Selecione a dificuldade:")
	print("<1>Fácil 	(30 aventureiros)")
	print("<2>Médio 	(18 aventureiros)")
	print("<3>Difícil 	(09 aventureiros)")
	print("<4>Sair do jogo =(")

	dif = int(input("\nEscolha entre as dificuldades 1, 2 ou 3:\n> "))
	num_aventureiros = 18

	if dif == 1:
		print("Dificuldade fácil escolhida!")
		num_aventureiros = 30
	elif dif == 2:
		print("Dificuldade média escolhida!")
		num_aventureiros = 18
	elif dif == 3:
		print("Dificuldade difícil escolhida!")
		num_aventureiros = 9
	elif dif == 4:
		exit()
	else:
		print("Você irá jogar com a dificuldade padrão (Médio)\n\n")

	aventureiros = []
	flag = 0

	print('\nA seguir você irá escolher a quantidade de aventureiros para cada classe.')
	print('Os druids causam 5 de dano veneno por ataque.')
	print('Já os mages possuem 4 de dano mágico.')
	print('Os guerreiros dão 6 de dano físico com seu ataque.\n')
	while flag == 0:
		n_druids = int(input("Escolha a quantidade de druids da sua equipe: "))
		if (num_aventureiros - n_druids) >= 0:
			flag = 1
			num_aventureiros = num_aventureiros - n_druids
			print("Você adicionou " + str(n_druids) + " druids!")
			while n_druids > 0:
				druid = Druid()
				avent = Aventureiro("druid", druid.dano, druid.tipo_dano)
				aventureiros.append(avent)
				n_druids -= 1
		else:
			print("Quantidade de druids selecionada é maior do que o seu número de aventureiros!\nDigite uma quantidade menor.")
	
	print("Ainda restam " + str(num_aventureiros) + " aventureiros para adicionar à sua equipe!")
	flag = 0

	while flag == 0:
		n_mages = int(input("\nEscolha a quantidade de mage da sua equipe: "))
		if (num_aventureiros - n_mages) >= 0:
			flag = 1
			num_aventureiros = num_aventureiros - n_mages
			print("Você adicionou " + str(n_mages) + " mages!")
			while n_mages > 0:
				mage = Mage()
				avent = Aventureiro("mage", mage.dano, mage.tipo_dano)
				aventureiros.append(avent)
				n_mages -= 1
		else:
			print("Quantidade de mages selecionada é maior do que o seu número de aventureiros!\nDigite uma quantidade menor.")
	
	print("Ainda restam " + str(num_aventureiros) + " aventureiros para adicionar à sua equipe!")
	flag = 0

	while flag == 0:
		n_warrior = int(input("\nEscolha a quantidade de guerreiros da sua equipe: "))
		if (num_aventureiros - n_warrior) >= 0:
			flag = 1
			num_aventureiros = num_aventureiros - n_warrior
			print("Você adicionou " + str(n_warrior) + " guerreiros!")
			while n_warrior > 0:
				warrior = Warrior()
				avent = Aventureiro("warrior", warrior.dano, warrior.tipo_dano)
				aventureiros.append(avent)
				n_warrior -= 1
		else:
			print("Quantidade de guerreiros selecionada é maior do que o seu número de aventureiros!\nDigite uma quantidade menor.")

	print("\nEquipe pronta!\nVocê tem " + str(len(aventureiros)) + " aventureiros na sua equipe.")
	print_aventureiros(aventureiros)

	#iniciar a partida com a fila de monstros aleatórios pro level 1
	monstros = []
	lvl = 1

	while len(aventureiros) > 0:
		monstros = gerar_monstros(lvl)
		print_monstros(monstros)
		aventureiros = rounds(aventureiros, monstros)
		lvl += 1

def main():
	print("\n/*/*/*/* JOGO DE EXPLORACAO DA MASMORRA */*/*/*/")
	jogo()
	

main()
