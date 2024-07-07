#Ichou Aymane
#EXERCICE 1 

import Crypto.Util.number as cun 
import hashlib

def gen_rsa_keypair(bits): # Genere qu'une seule clé pour UNE personne 
	demi = bits //2
	p = cun.getPrime(demi)
	q = cun.getPrime(demi)
	n = p*q 
	phi_n = (p-1) * (q-1)
	e = cun.getPrime(6)
	assert(cun.GCD(e,phi_n) == 1) 
	d = cun.inverse(e,phi_n)
	return [(e, n ),(d , n)] # clef(publique,privé)





#Exercice 2

# Implémentez la fonction rsa qui prend en paramètre un message (représenté par un entier) et une clef
# (représentée par une paire comprenant un exposant et un module) et qui fait l’exponentiation modulaire.

def chiffrer_rsa (message, clef):
	return pow(message, clef[0], clef[1])


def dechiffrer_rsa(message_code , clef) : 
	return pow(message_code, clef[0] , clef[1])


key_a, key_b = gen_rsa_keypair(1024)

def rsa_enc(message, clef): 
	msg = int.from_bytes(message.encode('utf-8'), 'big')
	msg1 = chiffrer_rsa(msg, clef)
	return msg1 

def rsa_dec(message_enc, clef): 
	msg = dechiffrer_rsa(message_enc, clef)
	msg = msg.to_bytes((msg.bit_length() + 7) // 8, 'big').decode('utf-8')
	return msg 

#Simulation de la discussion 

alice = gen_rsa_keypair(512)
bob = gen_rsa_keypair(512)
print("Bob envoie un message à Alice :") 
message_bob = "salut beauté"
message_bob = rsa_enc(message_bob, alice[0])
print("Alice ouvre le message") 


message_bob = rsa_dec(message_bob, alice[1])
print("message bob :", message_bob)



#Exercice 3 

def h (entier) : 
	hache = hashlib.sha256()
	entier_bytes = entier.to_bytes(64, byteorder='big')
	hache.update(entier_bytes)
	hexa_hache = hache.hexdigest() 

	decimal_hache = int(hexa_hache,16)
	return decimal_hache


def rsa_sign(message , clef_pv) : 
	hach = h(message)
	s = chiffrer_rsa(hach, clef_pv)
	return(message, s)

def rsa_verify(message, cle_pub):
	print(cle_pub)
	signature = dechiffrer_rsa(message[1] , cle_pub)
	hach_mess = h(message[0])
	if(hach_mess == signature ):
		print("Good")
		return 1
	else :
		print("Attention, arnaque !")
		return 0 

test = rsa_sign(3647, bob[1])
test = rsa_verify(test,bob[0])
print(test) 

#-------------Exercice 4---------------------

# La version de RSA qu’on a implémentée ici, qu’on appelle communément textbook RSA, souffre de plusieurs
# problème de sécurité.
# Par exemple, il est possible de forger des chiffrés valides à partir,
# de chiffrés existants qu’on aurait interceptés.
# C’est ce qu’on appelle la malléabilité.
# → Comment ?

# Il est possbile que si on multiplie le chiffré intercepté par un nombre, on obtienne un message clair valide, 
# L'addition et la soustraction peuvent aussi fonctionner si la tiers opérande est bien choisi . 
# Cela étant donné de la base mathématique de l'algorithme RSA 


# 2. Un autre soucis est le déterminisme du chiffrement. C’est à dire que si on chiffre deux fois le même message
# avec la même clef, on obtient deux fois le même chiffré.
# → En quoi est-ce un problème ?

# L'attaquant sait si le contenu du message change ou non.
# Ce qui donne des indices sur le contenu du message, or , notre message doit être chiffré. 
# Par exemple, lorsque les messages suivent un protocole bien précis, on peut en déduire le contenu ou bien,
# la position du message chiffré intercepté dans le message chiffré principal. 