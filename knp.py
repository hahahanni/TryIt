'''
kamen nuzky papir ted !!!
'''
import random

#definice promenych

kamen = 1
nuzky = 2
papir = 3

vyherni_volba=[[1,2],[2,3],[3,1]]

#definice vyher
def urceni_vyhry(volba):
	if volba in vyherni_volba:
		print(volba, " \n Gratuluji, vyhrala jsi!")
	else:
		print(volba, " \n Zkus stesti priste")

again="ano"

while again=="ano":
	ja=int(input("Kamen (1), nuzky (2), papir (3), ted !!! \n Zadej svou volbu: "))
	pocitac = random.randint(1,3)
	volba=[ja,pocitac]
	urceni_vyhry(volba)
	again=input("Chces hrat znova? ano/ne : ")
	if again=="ne":
		"Tak cauuuu!"
		break