open Mips
open Mips_helper

let () =
  print_asm Stdlib.stdout
    { text = 
        def "main"
        (
          [Li (T0, 1)]
        )
        @def "while_0"
          ([Bgtu (T0, 2147483648, "sortie_while_0")
          ;Move (T1 , T0)])
        @def "while_1"
        (   [Blez(T1, "sortie_while_1")
            ;Li(T3,0)
            ;Andi(T2,T1,1)
            ;Beq(T2,T3,"else_0")])
        @def "if__"
          ((print_str "diez")
            @[J("suite_0")])
        @def "else_0"
        (print_str "space")

        @def "suite_0"
        (
          [Srl(T1,T1,1)
          ;J("while_1")]
        )
        @def "sortie_while_1"
        (
          (print_str "nl")
          @[Sll(T2,T0,1)]
          @[Xor(T0,T0,T2)]
          @[J("while_0")]          
        )
        @def "sortie_while_0"
        (
          [Li (T0, 1)]
        )


      ; data = [
          ("diez", Asciiz "#")
         ;("space", Asciiz " ")
         ;("nl", Asciiz "\\n")
      ]
    } 

