#Ichou Aymane L3B 
.text
.globl main

main: 

  #On demande la valeur n
  li $v0, 4
  la $a0, num1q
  syscall

  #On enregistre la valeur dans t0
  li $v0, 5
  syscall
  move $t0, $v0

  #On enregistre le cumul des operation dans s0
  li $t4 0 

  #On fait la boucle 
loop:
  beq $t0, $0, end_loop
  addi $t0, $t0, -1
  add $t4, $t4, $t0
  b loop
end_loop:
  
  #Affichage du resultat
  li $v0, 4
  la $a0, sum
  syscall

  move $a0,$t4
  li $v0, 1 
  syscall 

  li $v0, 4
  la $a0, nl
  syscall

  li $v0, 10
  syscall

.data
num1q: .asciiz "Please enter a number: "
sum:   .asciiz "Le résultat est : "
nl:    .asciiz "\n"