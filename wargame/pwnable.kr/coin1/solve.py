from pwn import *

p = remote("pwnable.kr", 9007)

p.recvuntil("- Ready? starting in 3 sec... -")
p.recv()

def calc(maximum, minimum):
    return int((maximum - minimum) / 2 + (0 if (maximum - minimum) % 2 is 0 else 1))



for i in range(100):
    rd = p.recv().strip()

    N = int(rd.split(" ")[0][2:])
    C = int(rd.split(" ")[1][2:])

    print("Stage %d : N is %d & C is %d" % (i+1, N, C))

    minimum = 0
    maximum = N

    for j in range(C + 1):
        lst = " ".join([str(n + minimum) for n in range(calc(maximum, minimum))])

        p.sendline(lst)
        print("minimum is %d and maxmimum is %d and output is %s" % (minimum, maximum, lst))

        rd = p.recv().strip()
        print("received : \"" + rd + "\"")
        
        if "Correct!" in rd:
            break

        value = int(rd)

        if maximum - minimum is 1:
            if value % 10 is 0:
                minimum += 1
                maximum += 1
            continue
        
        
        if value % 10 is 0:
            minimum += calc(maximum, minimum)
        else:
            maximum -= calc(maximum, minimum)
    
    print("Solve stage %d" % (i+1))

    # rd = rd.split("\n")[1]

    # N = int(rd.split(" ")[0][2:])
    # C = int(rd.split(" ")[1][2:])

p.interactive()