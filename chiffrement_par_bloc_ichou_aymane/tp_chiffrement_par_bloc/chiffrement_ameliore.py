#Ichou Aymane
#EXERCICE 1 


clef = ( 5, 11 )
substition_tab = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
substition_tab_inv = [substition_tab.index(i) for i in range(16)]
#Méthode pour inverser index et valeur ou on peut aussi le faire à la main 
print(substition_tab_inv)
def round(message, clef_val): 
	#Le parametre tour est soit 0 ou 1 
	#Le message est sur 4 bits ( compris entre 0 et 15)
	#La substitution table est donnée dans l'exo 
	m0 = message ^ clef_val
	chiffre_0 = substition_tab[m0] 
	return chiffre_0 


def enc(message) : 
	#Fonction qui réalise les tours(2)
	message_encode = round(message, clef[0])
	message_encode1 = round(message_encode, clef[1])
	return message_encode1


def back_round(message_chiffre, key) :
	message_chiffre = substition_tab_inv[message_chiffre]
	message_chiffre = message_chiffre ^ key
	return message_chiffre

def dec(message_chiffre): 
	message_chiffre = back_round(message_chiffre, clef[1]) 
	message_chiffre = back_round(message_chiffre, clef[0])
	return message_chiffre

print("----Test des fonctions enc et dec----")
message = 13
print("Message original:", message)
message_encode = enc(message)
print("Message encodé :", message_encode)
message_decode = dec(message_encode)
print("Message décodé :", message_decode)


#EXERCICE 2 -------------------------------------------------------

#Dans cet exo , les messages font 8bits
#Bourrage de bit 
def form_octet(binary) : 
	return format(binary , '08b')


def poids_fort(nombre) : 
	return nombre >> 4 

def poids_faible(nombre) : 
	return nombre & 15 #1111

def enc_byte(octet , clef):
	#On sépare le nibble gauche et droit
	nibble_gauche = poids_fort(octet)
	nibble_droit = poids_faible(octet)

	#On les encode chacuns de leurs côtés
	nibble_gauche = enc(nibble_gauche)
	nibble_droit = enc(nibble_droit)

	#On les concatène 
	res = (nibble_gauche<<4) | (nibble_droit)
	return res

def dec_byte(octet, clef): 
	nibble_gauche = poids_fort(octet)
	nibble_droit = poids_faible(octet)
	nibble_gauche = dec(nibble_gauche)
	nibble_droit = dec(nibble_droit)
	res = (nibble_gauche<<4) | (nibble_droit)
	return res 

#TEST de mes fonctions de recuperation de nibble
# a = 43
# print("53 en binaire :",bin(a))
# print("53 faible ", poids_faible(a))
# print("53 fort ", poids_fort(a))
message = 255
enc_mess = enc_byte(message,clef)
dec_mess = dec_byte(enc_mess, clef)

print("--------Test de enc_byte & dec_byte------------")
print("Message original :", message)
print("Message crypté :", enc_mess)
print("Message decrypté :" , dec_mess)

print("On vérifie qu'on sait encoder et décodes des caracteres ascii")
print("Print de ord() et chr()")
print(ord("a"))
print(chr(97))

def enc_file(file_name , key): 
	with open(file_name , 'rb') as open_file :
		texte_source = open_file.read()
		with open( file_name +".enc" , 'wb') as modified_file :
			for i in texte_source : 
				temp = enc_byte((i), key)
				modified_file.write(temp.to_bytes(1,"big"))

def dec_file(file_name , key, output): 
	with open(file_name , 'rb') as open_file :
		texte_source = open_file.read()
	with open( output , 'wb') as modified_file :
		for i in texte_source : 
			temp = dec_byte(i , key )
			modified_file.write(temp.to_bytes(1,"big"))

enc_file('bonjour.txt', clef)
dec_file('bonjour.txt.enc', clef , "coucou.txt")

#EXERCICE 3 

#Question 1:
enc_file('test.txt' , (9,0))

#On peut remarquer une répétition dans les caractères du fichier encodé au même titre que les lettres de coucou
#Comme type d'attaque on peut imaginer une analyse de fréquence afin d'essayer d'associer chaque caractère chiffré
#à son caractère clair. Etant donné que pour une même clé, chaque caractere chiffré correspondra à un seul et unique 
#caractère en clair.  

def	cbc_enc_file(file_name , key, vecteur_init) : 
	with open(file_name , 'rb') as open_file : 
		texte_source = open_file.read()
		message_prec = vecteur_init

	with open( file_name +".enc" , 'wb') as modified_file :
		for octet in texte_source:
			temp = message_prec ^ octet
			temp = enc_byte(temp , key)
			modified_file.write(temp.to_bytes(1,"big"))
			message_prec = temp 

def	cbc_dec_file(encoded_file , key, init_vecteur ,output ) : 
	with open(encoded_file , 'rb') as open_file :
		texte_source = open_file.read()
		open_file_convert = []
		for i in texte_source : 
			open_file_convert.append(i)
		#On inverse car on déchiffre, on part donc de la fin 
		open_file_convert.reverse()

	with open( output , 'wb') as modified_file :
		for i in range(0, len(open_file_convert) - 1) : 
			#Cette fois ci on decode, puis XOR message clair avec suivant chiffré
			open_file_convert[i] = dec_byte(open_file_convert[i] , key) 
			open_file_convert[i] = open_file_convert[i+1] ^ open_file_convert[i]
		#On traite le dernier cas, ou il faut XOR avec le vecteur d'init
		open_file_convert[-1] = dec_byte(open_file_convert[-1], key)
		open_file_convert[-1] = open_file_convert[-1] ^ init_vecteur
		#On reversed() pour éviter d'avoir le message avec un ordre de lettre inversé
		for octet in reversed(open_file_convert) : 
			modified_file.write(octet.to_bytes(1,"big"))




		

vecteur = 5
cbc_enc_file("test.txt" , (9,0), vecteur)
cbc_dec_file("test.txt.enc", (9,0) , vecteur , "correction.txt" )


# Quel est l’avantage de la génération aléatoire du vecteur d’initialisation ?
	#Meme si on possede la meme clé, le vecteur d'initiliation empêche le décodage. 
	#Il faut désormais que le message, la clé, et le vecteur d'initialition soit le même pour les deux personnes
