.text 

.globl main


main : 
	addi $sp, $sp, -4 
	sw $ra, 0($sp)

	li $t0, 6
	andi $t1, $t0, 1 
	beq $t1, 0, else_0

	#if implicite , si t0 impaire
	li $v0, 4
	la $a0, diez
	syscall
	j fin

else_0: 
	#si t0 paire
	li $v0, 4
	la $a0, space
	syscall 

fin:
	lw $ra, 0($sp)
	addi $sp, $sp, 4

	jr $ra

.data 

diez:  .asciiz"impaire \n"
space: .asciiz"paire\n "
nada:  .asciiz""