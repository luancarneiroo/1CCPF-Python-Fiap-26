escolhadousuario = 2
# 0 -> sair do programa
# 1 -> entrar no programa
# -> erro!!

match escolhadousuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("ERRO!")