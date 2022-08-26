def tabuleiro():
    for i in lista:
        for j in i:
            print(j, end=' ')
        print()

lista = [
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
]

print("Jogo da Velha")
print("\nInstrução:")
print("Você irá informar a linha e depois a coluna a cada rodada.")
print('''
      1 2 3
    1 _ _ _
    2 _ _ _
    3 _ _ _''')
print()

for a in range(1,10):
    print(f"Rodada {a}")
    while a%2 != 0:
        linha = int(input("Insira a linha: "))
        coluna = int(input("Insira a coluna: "))
        if lista[linha-1][coluna-1] == '_':
            lista[linha-1][coluna-1] = 'X'
            tabuleiro()
            print()
            break
        else:
            print("Jogada Inválida!")
            print()
    while a%2 == 0:
        if a == 2:
            if lista[1][1] == '_':
                lista[1][1] = 'O'
                tabuleiro()
                break
            else:
                lista[0][0] = 'O'
                tabuleiro()
                break
        elif a == 4:
            if lista[1][1] == 'O':
                if lista[0][0] == 'X' and lista[0][1] == 'X':
                    lista[0][2] = 'O'
                    tabuleiro()
                    break
                if lista[0][0] == 'X' and lista[0][2] == 'X':
                    lista[0][1] = 'O'
                    tabuleiro()
                    break
                if lista[0][1] =='X' and lista[0][2]=='X':
                    lista[0][0] ='O'
                    tabuleiro()
                    break
                if lista[0][0] == 'X' and lista[1][0] =='X':
                    lista[2][0] = 'O'
                    tabuleiro()
                    break
                if lista[0][0] == 'X' and lista[2][0] =='X':
                    lista[1][0] = 'O'
                    tabuleiro()
                    break
                if lista[1][0] == 'X' and lista[2][0] =='X':
                    lista[0][0] = 'O'
                    tabuleiro()
                    break
                if lista[2][0] == 'X' and lista[2][1] == 'X':
                    lista[2][2] = 'O'
                    tabuleiro()
                    break
                if lista[2][0] == 'X' and lista[2][2] == 'X':
                    lista[2][1] = 'O'
                    tabuleiro()
                    break
                if lista[2][1] =='X' and lista[2][2]=='X':
                    lista[2][0] ='O'
                    tabuleiro()
                    break 
                if lista[1][0] =='X' and lista[1][2] == 'X':
                    lista[0][1] ='O'
                    tabuleiro()
                    break
                if lista[2][2] == 'X' and lista[1][2] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X' and lista[0][2] == 'X':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'X' and lista[1][2] == 'X':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                else:
                    achou = False
                    for a in range(2):
                        for b in range(2):
                            if lista[a][b] == '_':
                                lista[a][b] = 'O'
                                tabuleiro()
                                achou = True
                                break
                        if achou:
                            break
                    if achou:
                        break
            else:
                if lista[0][1] == 'X':
                    lista[2][1] = 'O'
                    tabuleiro()
                    break
                if lista[0][2] == 'X':
                    lista[2][0] = 'O'
                    tabuleiro()
                    break
                if lista[1][2] == 'X':
                    lista[1][0] = 'O'
                    tabuleiro()
                    break
                if lista[2][2] == 'X':
                    lista[0][2] = 'O'
                    tabuleiro()
                    break
                if lista[2][1] == 'X':
                    lista[0][1] = 'O'
                    tabuleiro()
                    break
                if lista[2][0] == 'X':
                    lista[0][2] = 'O'
                    tabuleiro()
                    break
                if lista[1][0] == 'X':
                    lista[1][2] = 'O'
                    tabuleiro()
                    break
                else:
                    achou = False
                    for a in range(2):
                        for b in range(2):
                            if lista[a][b] == '_':
                                lista[a][b] = 'O'
                                tabuleiro()
                                achou = True
                                break
                        if achou:
                            break
                    if achou:
                        break
        elif a == 6:
            if lista[1][1] == 'O':
                if lista[0][0] == 'O':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] == 'O':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'O':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][2] == 'O':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'O':
                    if lista[0][0] == '_':
                        lista[0][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] == 'O':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'O':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'O':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[0][1] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[0][2] == 'X':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] =='X' and lista[0][2]=='X':
                    if lista[0][0] == '_':
                        lista[0][0] ='O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[1][0] =='X':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[2][0] =='X':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'X' and lista[2][0] =='X':
                    if lista[0][0] == '_':
                        lista[0][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'X' and lista[2][1] == 'X':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'X' and lista[2][2] == 'X':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] =='X' and lista[2][2]=='X':
                    if lista[2][0] == '_':
                        lista[2][0] ='O'
                        tabuleiro()
                        break 
                if lista[1][0] =='X' and lista[1][2] == 'X':
                    if lista[0][1] == '_':
                        lista[0][1] ='O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X' and lista[1][2] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X' and lista[0][2] == 'X':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'X' and lista[1][2] == 'X':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                else:
                    achou = False
                    for a in range(2):
                        for b in range(2):
                            if lista[a][b] == '_':
                                lista[a][b] = 'O'
                                tabuleiro()
                                achou = True
                                break
                        if achou:
                            break
                    if achou:
                        break
            else:
                if lista[0][0] == 'O' and lista[0][1] == 'O':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'O' and lista[0][2] == 'O':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] =='O' and lista[0][2]=='O':
                    if lista[0][0] == '_':
                        lista[0][0] ='O'
                        tabuleiro()
                        break
                if lista[0][0] == 'O' and lista[1][0] =='O':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'O' and lista[2][0] =='O':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'O' and lista[2][0] =='O':
                    if lista[0][0] == '_':
                        lista[0][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'O' and lista[2][1] == 'O':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'O' and lista[2][2] == 'O':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] =='O' and lista[2][2]=='O':
                    if lista[2][0] == '_':
                        lista[2][0] ='O'
                        tabuleiro()
                        break 
                if lista[1][0] =='O' and lista[1][2] == 'O':
                    if lista[0][1] == '_':
                        lista[0][1] ='O'
                        tabuleiro()
                        break
                if lista[2][2] == '0' and lista[1][2] == '0':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == '0' and lista[0][2] == '0':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == '0' and lista[1][2] == '0':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] == 'X':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'X':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][2] == 'X':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] == 'X':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'X':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                else:
                    achou = False
                    for a,b in enumerate(lista):
                        for c,d in enumerate(b):
                            if d == '_':
                                lista[a][c] = 'O'
                                tabuleiro()
                                achou = True
                                break
                        if achou:
                            break
                    if achou:
                        break
        else:
            if lista[1][1] == 'O':
                if lista[0][0] == 'O':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] == 'O':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'O':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][2] == 'O':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'O':
                    if lista[0][0] == '_':
                        lista[0][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] == 'O':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'O':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'O':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[0][1] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[0][2] == 'X':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] =='X' and lista[0][2]=='X':
                    if lista[0][0] == '_':
                        lista[0][0] ='O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[1][0] =='X':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'X' and lista[2][0] =='X':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'X' and lista[2][0] =='X':
                    if lista[0][0] == '_':
                        lista[0][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'X' and lista[2][1] == 'X':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'X' and lista[2][2] == 'X':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] =='X' and lista[2][2]=='X':
                    if lista[2][0] == '_':
                        lista[2][0] ='O'
                        tabuleiro()
                        break 
                if lista[1][0] =='X' and lista[1][2] == 'X':
                    if lista[0][1] == '_':
                        lista[0][1] ='O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X' and lista[1][2] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X' and lista[0][2] == 'X':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'X' and lista[1][2] == 'X':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                else:
                    achou = False
                    for a in range(2):
                        for b in range(2):
                            if lista[a][b] == '_':
                                lista[a][b] = 'O'
                                tabuleiro()
                                achou = True
                                break
                        if achou:
                            break
                    if achou:
                        break    
            else:
                if lista[0][0] == 'O' and lista[0][1] == 'O':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'O' and lista[0][2] == 'O':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] =='O' and lista[0][2]=='O':
                    if lista[0][0] == '_':
                        lista[0][0] ='O'
                        tabuleiro()
                        break
                if lista[0][0] == 'O' and lista[1][0] =='O':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[0][0] == 'O' and lista[2][0] =='O':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'O' and lista[2][0] =='O':
                    if lista[0][0] == '_':
                        lista[0][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'O' and lista[2][1] == 'O':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'O' and lista[2][2] == 'O':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] =='O' and lista[2][2]=='O':
                    if lista[2][0] == '_':
                        lista[2][0] ='O'
                        tabuleiro()
                        break 
                if lista[1][0] =='O' and lista[1][2] == 'O':
                    if lista[0][1] == '_':
                        lista[0][1] ='O'
                        tabuleiro()
                        break
                if lista[2][2] == 'O' and lista[1][2] == 'O':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'O' and lista[0][2] == 'O':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'O' and lista[1][2] == 'O':
                    if lista[2][2] == '_':
                        lista[2][2] = 'O'
                        tabuleiro()
                        break
                if lista[0][1] == 'X':
                    if lista[2][1] == '_':
                        lista[2][1] = 'O'
                        tabuleiro()
                        break
                if lista[0][2] == 'X':
                    if lista[2][0] == '_':
                        lista[2][0] = 'O'
                        tabuleiro()
                        break
                if lista[1][2] == 'X':
                    if lista[1][0] == '_':
                        lista[1][0] = 'O'
                        tabuleiro()
                        break
                if lista[2][2] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[2][1] == 'X':
                    if lista[0][1] == '_':
                        lista[0][1] = 'O'
                        tabuleiro()
                        break
                if lista[2][0] == 'X':
                    if lista[0][2] == '_':
                        lista[0][2] = 'O'
                        tabuleiro()
                        break
                if lista[1][0] == 'X':
                    if lista[1][2] == '_':
                        lista[1][2] = 'O'
                        tabuleiro()
                        break
                else:
                    achou = False
                    for a,b in enumerate(lista):
                        for c,d in enumerate(b):
                            if d == '_':
                                lista[a][c] = 'O'
                                tabuleiro()
                                achou = True
                                break
                        if achou:
                            break
                    if achou:
                        break      
    #Condição para Jogador ganhar
    if lista[0][0] == 'X' and  lista[0][1]== 'X' and lista[0][2] == 'X':
        print("Jogador Ganhou!") 
        break
    if lista[0][0] == 'X' and  lista[1][1]== 'X' and lista[2][2] == 'X':
        print("Jogador Ganhou!") 
        break
    if lista[0][2] == 'X' and  lista[1][1]== 'X' and lista[2][0] == 'X':
        print("Jogador Ganhou!") 
        break
    if lista[1][0] == 'X' and  lista[1][1]== 'X' and lista[1][2] == 'X':
        print("Jogador Ganhou!") 
        break
    if lista[2][0] == 'X' and  lista[2][1]== 'X' and lista[2][2] == 'X':
        print("Jogador Ganhou!") 
        break
    if lista[0][0] == 'X' and  lista[1][0]== 'X' and lista[2][0] == 'X':
        print("Jogador Ganhou!") 
        break
    elif lista[0][1] == 'X' and  lista[1][1]== 'X' and lista[2][1] == 'X':
        print("Jogador Ganhou!") 
        break    
    if lista[0][2] == 'X' and  lista[1][2]== 'X' and lista[2][2] == 'X':
        print("Jogador Ganhou!") 
        break 
    
    #Condição para Computador Ganhar
    if lista[0][0] == 'O' and  lista[0][1]== 'O' and lista[0][2] == 'O':
        print("Computador Ganhou!") 
        break
    if lista[0][0] == 'O' and  lista[1][1]== 'O' and lista[2][2] == 'O':
        print("Computador Ganhou!") 
        break
    if lista[0][2] == 'O' and  lista[1][1]== 'O' and lista[2][0] == 'O':
        print("Computador Ganhou!")  
        break
    if lista[1][0] == 'O' and  lista[1][1]== 'O' and lista[1][2] == 'O':
        print("Computador Ganhou!")  
        break
    if lista[2][0] == 'O' and  lista[2][1]== 'O' and lista[2][2] == 'O':
        print("Computador Ganhou!")  
        break
    if lista[0][0] == 'O' and  lista[1][0]== 'O' and lista[2][0] == 'O':
        print("Computador Ganhou!")  
        break
    if lista[0][1] == 'O' and  lista[1][1]== 'O' and lista[2][1] == 'O':
        print("Computador Ganhou!")  
        break    
    if lista[0][2] == 'O' and  lista[1][2]== 'O' and lista[2][2] == 'O':
        print("Computador Ganhou!")  
        break 
    #Empate
    empate = True
    for m in lista:
        for n in m:
            if n == '_':
                empate = False
                break
    if empate:
        print("Empate!")
        break
