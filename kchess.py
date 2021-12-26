top_moves = []
class moves:
    mov_a1= ['b3', 'c2']
    mov_b1= ['a3', 'c3', 'd2']
    mov_c1= ['a2', 'b3', 'd3', 'e2']
    mov_d1= ['b2', 'c3', 'e3', 'f2']
    mov_e1= ['c2', 'd3', 'f3', 'g2']
    mov_f1= ['d2', 'e3', 'g3', 'h2']
    mov_g1= ['h3', 'f3', 'e2']
    mov_h1= ['f2', 'g3']
    mov_a2= ['f8', 'c3', 'g5']
    mov_b2= ['a4', 'c4', 'd3', 'd1']
    mov_c2= ['a1', 'a3', 'b4', 'd4', 'e3', 'e1']
    mov_d2= ['b1', 'b3', 'c4', 'e4', 'f3', 'f1']
    mov_e2= ['c1', 'c3', 'd4', 'f4', 'g3', 'g1']
    mov_f2= ['d1', 'd3', 'e4', 'g4', 'h3', 'h1']
    mov_g2= ['e1', 'e3', 'f4', 'h4']
    mov_h2= ['f1', 'f3', 'g4']
    mov_a3= ['b5', 'c4', 'c2', 'b1']
    mov_b3= ['a5', 'c5', 'd4', 'd2', 'c1', 'a1']
    mov_c3= ['a4', 'b5', 'a2', 'e4', 'e2', 'd1', 'b1', 'd5']
    mov_d3= ['b4', 'c5', 'b2', 'f4', 'f2', 'e1', 'c1', 'e5']
    mov_e3= ['c4', 'd5', 'c2', 'g4', 'g2', 'f1', 'd1', 'f5']
    mov_f3= ['d4', 'e5', 'd2', 'h4', 'h2', 'g1', 'e1', 'g5']
    mov_g3= ['h5', 'f5', 'e4', 'e2', 'f1', 'h1']
    mov_h3= ['g5', 'f4', 'f2', 'g1']
    mov_a4= ['b6', 'c5', 'c3', 'b2']
    mov_b4= ['a6', 'c6', 'd5', 'd3', 'c2', 'a2']
    mov_c4= ['a5', 'b6', 'a3', 'e5', 'e3', 'd2', 'b2', 'd6']
    mov_d4= ['b5', 'c6', 'b3', 'f5', 'f3', 'e2', 'c2', 'e6']
    mov_e4= ['c5', 'd6', 'c3', 'g5', 'g3', 'f2', 'd2', 'f6']
    mov_f4= ['d5', 'e6', 'd3', 'h5', 'h3', 'g2', 'e2', 'g6']
    mov_g4= ['h6', 'f6', 'e5', 'e3', 'f2', 'h2']
    mov_h4= ['g6', 'f5', 'f3', 'g2']
    mov_a5= ['b7', 'c6', 'c4', 'b3']
    mov_b5= ['a7', 'c7', 'd6', 'd4', 'c3', 'a3']
    mov_c5= ['a6', 'b7', 'a4', 'e6', 'e4', 'd3', 'b3', 'd7']
    mov_d5= ['b6', 'c7', 'b4', 'f6', 'f4', 'e3', 'c3', 'e7']
    mov_e5= ['c6', 'd7', 'c4', 'g6', 'g4', 'f3', 'd3', 'f7']
    mov_f5= ['d6', 'e7', 'd4', 'h6', 'h4', 'g3', 'e3', 'g7']
    mov_g5= ['h7', 'f7', 'e6', 'e4', 'f3', 'h3']
    mov_h5= ['g7', 'f6', 'f4', 'g3']
    mov_a6= ['b8', 'c7', 'c5', 'b4']
    mov_b6= ['a8', 'c8', 'd7', 'd5', 'c4', 'a4']
    mov_c6= ['a7', 'b8', 'a5', 'e7', 'e5', 'd4', 'b4', 'd8']
    mov_d6= ['b7', 'c8', 'b5', 'f7', 'f5', 'e4', 'c4', 'e8']
    mov_e6= ['c7', 'd8', 'c5', 'g7', 'g5', 'f4', 'd4', 'f8']
    mov_f6= ['d7', 'e8', 'd5', 'h7', 'h5', 'g4', 'e4', 'g8']
    mov_g6= ['h8', 'f8', 'e7', 'e5', 'f4', 'h4']
    mov_h6= ['g8', 'f7', 'f5', 'g4']
    mov_a7= ['c8', 'c6', 'd7']
    mov_b7= ['d8', 'd6', 'c5', 'a5']
    mov_c7= ['a8', 'a6', 'b5', 'd5', 'e6', 'e8']
    mov_d7= ['b8', 'b6', 'c5', 'e5', 'f6', 'f8']
    mov_e7= ['c8', 'c6', 'd5', 'f5', 'g6', 'g8']
    mov_f7= ['d8', 'd6', 'e5', 'g5', 'h6', 'h8']
    mov_g7= ['e8', 'e6', 'f5', 'h5']
    mov_h7= ['c1', 'f6', 'b4']
    mov_a8= ['b6', 'c7']
    mov_b8= ['a6', 'c6', 'd7']
    mov_c8= ['a7', 'b6', 'd6', 'e7']
    mov_d8= ['b7', 'c6', 'e6', 'f7']
    mov_e8= ['c7', 'd6', 'f6', 'g7']
    mov_f8= ['d7', 'e6', 'g6', 'h7']
    mov_g8= ['h6', 'f6', 'e7']
    mov_h8= ['f7', 'g6']
class passado:
    pass_2 = []
    pass_3 = []
    pass_4 = []
    pass_5 = []
    pass_6 = []
    pass_7 = []
    pass_8 = []
    pass_9 = []
    pass_10 = []
    pass_11 = []
    pass_12 = []
    pass_13 = []
    pass_14 = []
    pass_15 = []
    pass_16 = []
    pass_17 = []
    pass_18 = []
    pass_19 = []
    pass_20 = []
objeto = passado()
def evaluate(PMI,PMF,count_current_moves):
    global count_top_moves
    global top_moves
    global objeto
    count_current_moves += 1
    for i in range(len(PMI)):
        if count_current_moves > count_top_moves:
            break
        pasado = "pass_" + str(count_current_moves)
        pisado = list(getattr(objeto,pasado))
        nuevo = "pass_" + str(count_current_moves+1)
        setattr(objeto, nuevo, [])
        pisado.append(PMI[i])
        setattr(objeto, nuevo, pisado)
        puntonuevo = "mov_" + PMI[i]
        movnuevos = list(getattr(moves,puntonuevo))
        for y in range(len(pisado)):
            if pisado[y] in movnuevos:
                movnuevos.remove(pisado[y])
        for x in range(len(movnuevos)):
            if movnuevos[x] in PMF: 
                if  count_current_moves < count_top_moves:
                    count_top_moves = count_current_moves
                    new = []
                    new = list(getattr(objeto,nuevo))
                    new.append(movnuevos[x])
                    top_moves = list(new)
                elif count_current_moves == count_top_moves:
                    top_moves += "ó"
                    new = []
                    new = list(getattr(objeto,nuevo))
                    new.append(movnuevos[x])
                    top_moves += new
        evaluate(movnuevos,PMF,count_current_moves)
    
def main():

    global posición_final
    global posición_inicial
    global count_top_moves
    global objeto
    posición_inicial = input()
    posición_final = input()
    Lugar_inicial = "mov_" + posición_inicial
    Lugar_final = "mov_" + posición_final
    PMI = getattr(moves,Lugar_inicial)
    PMF = getattr(moves,Lugar_final)
    passado.pass_3 = [posición_inicial]

    current_moves = []
    global top_moves
    count_current_moves = 1
    count_top_moves = 1000000
    count2 = False
    

    # directo
    if posición_final in PMI:
            count_top_moves = 1
            print("top moves = " + str(count_top_moves))
            exit()
    # 2   
    count_current_moves += 1
    for i in range(len(PMI)):
        if PMI[i] in PMF:
            current_moves = []
            current_moves.append(PMI[i])
            if  count_current_moves < count_top_moves:
                count_top_moves = count_current_moves
                top_moves = list(current_moves)
                count2 = True
            elif count_current_moves == count_top_moves:
                top_moves += "ó"
                top_moves += current_moves
    if count2 == True:
        print(top_moves)
        print(count_top_moves)
        exit()
    # 3 o mas
    evaluate(PMI,PMF,count_current_moves)
    print(top_moves)
    print(count_top_moves)
main()