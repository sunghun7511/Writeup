inputlist = list()
final_str = ""

randlist = list()

inputlist.append(0)
inputlist.append(0)
for i in range(126):
    inputlist.append(1)

'''
for i in range(0x2000 - 128):
    inputlist.append(0)
'''

f = open("rand_data", "r")
randlist = str(f.read()).strip().split("\n")
f.close()

print("[*] random list complete : " + str(len(randlist)))

tmp = 0

def un_swap():
    global tmp
    l = len(inputlist)

    for i in range(l):
        print(len(randlist) - 1 - tmp)
        rand = int(randlist[len(randlist) - 1 - tmp])
        print(rand)
        if i != rand:
            inputlist[i], inputlist[rand] = inputlist[rand], inputlist[i]
        tmp = tmp + 1
    return

'''
        tmp = 1;
        for ( l = 0; l < 8 * v8; ++l ) {
            if ( v9[l] )
                tmp ^= 1u;
            v9[l] = tmp;
        }
'''
def un_bits():
    l = len(inputlist)
    last = 0

    for i in range(l):
        if inputlist[i] != last:
            inputlist[i] = 1
        else:
            inputlist[i] = 0
        last = inputlist[i]
    return

for i in range(16):
    un_swap()
    un_bits()


for i in range(16):
    tmp = 0
    for j in range(8):
        tmp = tmp ^ (inputlist[i*8 + j] << j)
    final_str = final_str + chr(tmp)
    print(final_str)

print(final_str)