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

def main():
	print("JOGO EXPLORACAO MASMORRA")
	druid = Druid()
	avent = Aventureiro("druid", druid.dano, druid.tipo_dano)
	print(avent.classe)
	print(avent.dano)
	print(avent.tipo_dano)

main()
