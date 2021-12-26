tablero = [["a8","b8","c8","d8","e8","f8","g8","h8"],
        ["a7","b7","c7","d7","e7","f7","g7","h7"],
        ["a6","b6","c6","d6","e6","f6","g6","h6"],
        ["a5","b5","c5","d5","e5","f5","g5","h5"],
        ["a4","b4","c4","d4","e4","f4","g4","h4"],
        ["a3","b3","c3","d3","e3","f3","g3","h3"],
        ["a2","b2","c2","d2","e2","f2","g2","h2"],
        ["a1","b1","c1","d1","e1","f1","g1","h1"]]
        
#esquinas      

moves.mov_a8 = moves.mov_a8 = ["b6","c7"]
moves.mov_h8 = ["f7","g6"]
moves.mov_a1 = ["b3","c2"]
moves.mov_h1 = ["f2","g3"]

#semi esquinas   
# 8 y 1    
 
moves.mov_b8 = [tablero[2][0],tablero[2][2],tablero[1][3]]
moves.mov_g8 = [tablero[2][7],tablero[2][5],tablero[1][4]]
moves.mov_b1 = [tablero[5][0],tablero[5][2],tablero[6][3]]
moves.mov_g1 = [tablero[5][7],tablero[5][5],tablero[6][4]]

# 7 y 2
  
moves.mov_a7 = [tablero[0][2],tablero[2][2],tablero[1][3]]
moves.mov_h7 = [tablero[7][2],tablero[2][5],tablero[4][1]]
moves.mov_a2 = [tablero[0][5],tablero[5][2],tablero[3][6]]
moves.mov_h2 = [tablero[7][5],tablero[5][5],tablero[4][6]]   

# laterales 8

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c8 = [tablero[1][countL1],tablero[2][countL2],tablero[2][countL3],tablero[1][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d8 = [tablero[1][countL1],tablero[2][countL2],tablero[2][countL3],tablero[1][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e8 = [tablero[1][countL1],tablero[2][countL2],tablero[2][countL3],tablero[1][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f8 = [tablero[1][countL1],tablero[2][countL2],tablero[2][countL3],tablero[1][countL4]]

# laterales 1

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c1 = [tablero[6][countL1],tablero[5][countL2],tablero[5][countL3],tablero[6][countL4]]   
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d1 = [tablero[6][countL1],tablero[5][countL2],tablero[5][countL3],tablero[6][countL4]]  
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e1 = [tablero[6][countL1],tablero[5][countL2],tablero[5][countL3],tablero[6][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f1 = [tablero[6][countL1],tablero[5][countL2],tablero[5][countL3],tablero[6][countL4]]

# laterales a

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_a6 = [tablero[countL1][1],tablero[countL2][2],tablero[countL3][2],tablero[countL4][1]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_a5 = [tablero[countL1][1],tablero[countL2][2],tablero[countL3][2],tablero[countL4][1]]  
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_a4 = [tablero[countL1][1],tablero[countL2][2],tablero[countL3][2],tablero[countL4][1]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_a3 = [tablero[countL1][1],tablero[countL2][2],tablero[countL3][2],tablero[countL4][1]] 

# laterales h

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_h6 = [tablero[countL1][6],tablero[countL2][5],tablero[countL3][5],tablero[countL4][6]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_h5 = [tablero[countL1][6],tablero[countL2][5],tablero[countL3][5],tablero[countL4][6]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_h4 = [tablero[countL1][6],tablero[countL2][5],tablero[countL3][5],tablero[countL4][6]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_h3 = [tablero[countL1][6],tablero[countL2][5],tablero[countL3][5],tablero[countL4][6]]

# esquinas dentro del perimetro

moves.mov_b7 = ["d8","d6","c5","a5"]
moves.mov_g7 = ["e8","e6","f5","h5"]
moves.mov_b2 = ["a4","c4","d3","d1"]
moves.mov_g2 = ["e1","e3","f4","h4"]

# perimetro dentro del perimetro
    # lateral 7

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c7 = [tablero[0][countL1],tablero[2][countL1],tablero[3][countL2],tablero[3][countL3],tablero[2][countL4],tablero[0][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d7 = [tablero[0][countL1],tablero[2][countL1],tablero[3][countL2],tablero[3][countL3],tablero[2][countL4],tablero[0][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e7 = [tablero[0][countL1],tablero[2][countL1],tablero[3][countL2],tablero[3][countL3],tablero[2][countL4],tablero[0][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f7 = [tablero[0][countL1],tablero[2][countL1],tablero[3][countL2],tablero[3][countL3],tablero[2][countL4],tablero[0][countL4]]

    # lateral 2

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c2 = [tablero[7][countL1],tablero[5][countL1],tablero[4][countL2],tablero[4][countL3],tablero[5][countL4],tablero[7][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d2 = [tablero[7][countL1],tablero[5][countL1],tablero[4][countL2],tablero[4][countL3],tablero[5][countL4],tablero[7][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e2 = [tablero[7][countL1],tablero[5][countL1],tablero[4][countL2],tablero[4][countL3],tablero[5][countL4],tablero[7][countL4]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f2 = [tablero[7][countL1],tablero[5][countL1],tablero[4][countL2],tablero[4][countL3],tablero[5][countL4],tablero[7][countL4]]

    # lateral b

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_b6 = [tablero[countL1][0],tablero[countL1][2],tablero[countL2][3],tablero[countL3][3],tablero[countL4][2],tablero[countL4][0]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_b5 = [tablero[countL1][0],tablero[countL1][2],tablero[countL2][3],tablero[countL3][3],tablero[countL4][2],tablero[countL4][0]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_b4 = [tablero[countL1][0],tablero[countL1][2],tablero[countL2][3],tablero[countL3][3],tablero[countL4][2],tablero[countL4][0]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_b3 = [tablero[countL1][0],tablero[countL1][2],tablero[countL2][3],tablero[countL3][3],tablero[countL4][2],tablero[countL4][0]]

    #lateral g

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_g6 = [tablero[countL1][7],tablero[countL1][5],tablero[countL2][4],tablero[countL3][4],tablero[countL4][5],tablero[countL4][7]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_g5 = [tablero[countL1][7],tablero[countL1][5],tablero[countL2][4],tablero[countL3][4],tablero[countL4][5],tablero[countL4][7]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_g4 = [tablero[countL1][7],tablero[countL1][5],tablero[countL2][4],tablero[countL3][4],tablero[countL4][5],tablero[countL4][7]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_g3 = [tablero[countL1][7],tablero[countL1][5],tablero[countL2][4],tablero[countL3][4],tablero[countL4][5],tablero[countL4][7]]

#centro
    #lateral 6

count1 = 1
count0 = 0
count3 = 3
count4 = 4

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c6 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d6 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e6 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f6 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]

    #laterales 5

count1 += 1
count0 += 1
count3 += 1
count4 += 1

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c5 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d5 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e5 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f5 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]

    #laterales 4

count1 += 1
count0 += 1
count3 += 1
count4 += 1

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c4 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d4 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e4 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f4 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]

    #laterales 3

count1 += 1
count0 += 1
count3 += 1
count4 += 1

countL1 = 0
countL2 = 1
countL3 = 3
countL4 = 4
moves.mov_c3 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_d3 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_e3 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
countL1 += 1
countL2 += 1
countL3 += 1
countL4 += 1
moves.mov_f3 = [tablero[count1][countL1],tablero[count0][countL2],tablero[count3][countL1],tablero[count1][countL4],tablero[count3][countL4],tablero[count4][countL3],tablero[count4][countL2],tablero[count0][countL3]]
