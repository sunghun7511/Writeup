fp = open("thisflag", "rb")

reads = fp.read()[::-1]

fp.close()

fp2 = open("output.png", "wb")
fp2.write(reads)
fp2.close()
