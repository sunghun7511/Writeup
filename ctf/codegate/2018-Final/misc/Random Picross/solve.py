# -*- coding: utf-8 -*-

'''

    ██████╗  █████╗ ███╗   ███╗██████╗  ██████╗ ███╗   ███╗    ██████╗ ██╗ ██████╗██████╗  ██████╗ ███████╗███████╗
    ██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔═══██╗████╗ ████║    ██╔══██╗██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
    ██████╔╝███████║██╔████╔██║██║  ██║██║   ██║██╔████╔██║    ██████╔╝██║██║     ██████╔╝██║   ██║███████╗███████╗
    ██╔══██╗██╔══██║██║╚██╔╝██║██║  ██║██║   ██║██║╚██╔╝██║    ██╔═══╝ ██║██║     ██╔══██╗██║   ██║╚════██║╚════██║
    ██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝██║ ╚═╝ ██║    ██║     ██║╚██████╗██║  ██║╚██████╔╝███████║███████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝

█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
    

    [*] Codegate2018 Warming up Challenge for Junior
    [*] Solve 10 round, 20x20 Random Picross
    [*] If you don't know how to solve picross puzzle,
        please visit >>> https://www.thonky.com/picross/
    [*] Input Answer as One line with '.' and capital 'O', without space.
        System split your input into 20 letters and check the answer ([0][0]~[0][19] ... [19][0]~[19][19])
    

█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
    
[*] ROUND  1



				 4  1  3  1  4  3  3  1  8  2  1  3  4  3 20  3  2  1  3  2 

				 1  7  2  1  1  4  1  5  1  1  3  2  2  2     3  2  2  7  6 

				 2  3  1  3  1  1  1  1  3  5  4  5  2  4     1  1  3  3  6 

				 1  1 10  7 10  5  1  6  3  7  6  1  9  6     1  8  1  2  2 

				 8  2           2  3  2     1                 4     8       

				                   5                          1             

				- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
               10  9  | 
       1  1  3  9  2  | 
       1  5  1  5  2  | 
 2  1  3  1  1  1  1  | 
       1  4  1  3  1  | 
          3  1  4  8  | 
               15  3  | 
 2  1  1  3  1  1  3  | 
       5  1  2  5  2  | 
       1  1  4  3  2  | 
    1  3  1  2  2  2  | 
                  19  | 
      10  2  1  2  1  | 
             6  6  6  | 
          1  4  1 11  | 
             1  9  8  | 
             5  5  6  | 
    1  1  3  3  3  2  | 
       3  4  1  3  4  | 
    3  1  2  1  5  2  | 
[*] Answer >>> ^C

'''
from pwn import *
import nonogram_solver, sys
from nonogram.puzzle import Puzzle

p = remote("110.10.147.24", 9090)

for stage in range(10):
    p.recvuntil("[*] ROUND  ")

    print("[*] Stage " + p.recvuntil("\n").strip())

    horizontal = [list() for i in range(19)]
    vecs = list()

    recv_next = p.recvuntil("\n", drop=True)[5:-1]
    while "-" not in recv_next:
        recv = recv_next
        recv_next = p.recvuntil("\n", drop=True)[5:-1]
        if len(recv) == 0:
            continue
        print("\"" + recv + "\"")
        vecs.append("  " + recv)
    
    j = 0
    for i in range(19):
        for j in vecs:
            if j[(i+1)*3-1] == " ":
                break
            else:
                horizontal[i].insert(0, int(j[i*3:].split()[0]))
    
    vertical = [list() for i in range(19)]
    vecs = list()

    for i in range(19):
        recv = p.recvuntil("\n", drop=True)[:-2]
        print("\"" + recv + "\"")
        vecs.append(" " + recv)

    for ind, i in enumerate(vecs):
        j = 0
        while True:
            if (j+1)*3-1 >= len(i):
                break
            elif i[(j+1)*3-1] == " ":
                j += 1
                continue
            else:
                vertical[ind].insert(0, int(i[(j+1)*3-1:].split()[0]))
                j += 1

    print("Horizontal : " + str(horizontal))
    print("Vertical : " + str(vertical))

    puzzle = Puzzle(horizontal, vertical)

    # puzzle.spacer_offset_y = 19
    # puzzle.spacer_offset_x = 19
    puzzle.printt()

    # Step-by-step solver
    while True:
        if not puzzle.solve_step():
            print("no next solution step")
        puzzle.printt()

    # nonogram_solver.deduce(horizontal, vertical)

    # grid = nonogram_solver.go(horizontal, vertical)
    # w, h = len(grid[0]), len(grid)
    # for y in range(0, h):
    #     row = grid[y]
    #     for x in range(0, w):
    #         val = row[x]

    #         if val == nonogram_solver.SYMBOL_FILLED:
    #             sys.stdout.write("H")
    #         if val == nonogram_solver.SYMBOL_X:
    #             sys.stdout.write(".")
    #     print("")
