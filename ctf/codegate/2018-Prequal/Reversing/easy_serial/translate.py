def chrs(cs):
    n = ""
    for c in cs:
        n += chr(c)
    return n

def num(a):
	return (chr(a + ord('1')))

def lo(a):
	return (chr(a + ord('a')))

def up(a):
	return (chr(a + ord('A')))

flag = ""

flag += chrs((70, 108, 97, 103, 123, 83, 48, 109, 101, 48, 102, 85, 53))

flag += "#"

flag += chrs((52, 114, 51, 76, 48, 48, 107, 105, 110, 103))

flag += "#"

flag += up(0) + lo(19) + up(19) + lo(7) + num(2) + up(18) + lo(19) + num(3) + lo(17) + lo(18)

print(flag)