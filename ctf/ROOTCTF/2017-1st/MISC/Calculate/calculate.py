def one(num, size):
    r = num + size
    r += 915
    return r


def two(num, size):
    r = num - size
    r -= 372
    return r


def three(num, size):
    r = num ^ size
    r ^= 826
    return r


def four(num, size):
    size %= 32
    r = num >> (32 - size)
    b = (num << size) - (r << 32)
    return b + r


if __name__ == "__main__":
    result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360,
              4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
    string = raw_input("Input String : ")
    Number = []
    tmp = 0

    for i in string:
        Number.append(ord(i))

    for i in Number:
        Number[tmp] = one(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = two(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = three(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = four(i, 100)
        tmp += 1

    print Number
    if Number == result:
        print "Correct!!"
    else:
        print "Incorrect.."