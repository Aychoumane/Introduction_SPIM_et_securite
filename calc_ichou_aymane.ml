type expr = 
|Num of int 
|Add of expr * expr 
|Difference of expr * expr 
|Produit of expr * expr 
|Quotient of expr * expr 
|Modulo of expr * expr 

(*commentaire*)

(*Fonction qui effectue uniquement l'affichage*)
let rec format expression =
	match expression with 
		| Num n -> Printf.sprintf "%d" n 
		| Add (a , b) -> Printf.sprintf "%s + %s" (format a) (format b)
		| Difference(a , b) -> Printf.sprintf "%s - %s"  (format a) (format b) 
		| Produit(a , b) -> Printf.sprintf "%s * %s"  (format a) (format b)
		| Quotient(a , b) -> Printf.sprintf "%s / %s"  (format a) (format b) 
		| Modulo(a , b) -> Printf.sprintf "%s mod %s"  (format a) (format b) 
(*Fonction qui effectue le calcul*)
let rec eval e = 
	match e with 
		| Num n -> n 
		| Add (a,b) -> (eval a) + (eval b) 
		| Difference (a,b) -> (eval a) - (eval b)
		| Produit (a,b) -> (eval a) * (eval b)
		| Quotient (a,b) -> if b = (Num 0) then failwith "DIVISION PAR ZERO \n " else (eval a) / (eval b)
		| Modulo (a,b) -> (eval a) mod (eval b)

(*Notre main, il faut qu'il renvoie rien nulle part*)
let () =
	let exp = Quotient(Num 3, Num 0) in 
	print_endline(format(exp)) ; 
	Printf.printf "%d\n" (eval exp)