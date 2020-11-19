#JOGO EXPLORACAO MASMORRA
#Alunos: Gustavo Belançon Mendes - Hector Dorrighello Giacon

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
class Orc:
	def __init__(self):
		self.hp = 8
		self.reducao = "veneno"
		self.porc_reducao = 0.5

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

	#iniciar a partida com a fila de monstros aleatórios pro level 1

def main():
	print("\n/*/*/*/* JOGO DE EXPLORACAO DA MASMORRA */*/*/*/")
	jogo()
	

main()
