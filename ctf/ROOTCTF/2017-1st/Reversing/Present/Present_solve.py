'''
* 
* 보지마요 못풀었으니까..
* 
'''



import sys

Str = [0x47, 0x5B, 0x72, 0x49, 0x7B, 0x6D, 0x7F]
a2 = [0x46, 0x6F, 0x69, 0x64, 0x65, 0x69]
g_Str = [ord("F"), ord("L"), ord("A"), ord("G")]

key = [1, 22, 51, 34, 22, 43, 12, 34, 36, 54, 28]
key2 = [34, 42, 54, 33]

key2[1] = key[8]
key2[3] = key[10]

one = 1

for ind, i in enumerate(Str):
    temp = ind * ind ^ i
    sys.stdout.write(chr(temp ^ key[ind]))

for ind, i in enumerate(g_Str):
    temp = ind * ind ^ i
    sys.stdout.write(chr(temp ^ key2[ind]))

print("")