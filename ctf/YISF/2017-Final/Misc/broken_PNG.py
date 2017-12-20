import os, sys
from PIL import Image

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

for f1 in os.listdir("/mnt/e/대회/yisf 본선/Misc/Broken_PNG/"):
    first = ""
    second = ""
    third = ""
    for f2 in os.listdir("/mnt/e/대회/yisf 본선/Misc/Broken_PNG/" + f1):
        path = "/mnt/e/대회/yisf 본선/Misc/Broken_PNG/" + f1 + "/" + f2
        try:
            fh = open(path, "rb")
            b = fh.read()
            bl = len(b)
            
            if b[0] == 0x89 and b[1] == 0x50:
                first = path
            elif b[bl-1] == 0x82 and b[bl-2] == 0x60:
                third = path
            else:
                second = path
            
            fh.close()
        except:
            print("Error")

    path = "/mnt/e/대회/yisf 본선/Misc/Broken_PNG_out/" + f1 + ".png"
    
    wh = open(path, "wb+")

    fh = open(first, "rb")
    sh = open(second, "rb")
    th = open(third, "rb")
    
    wh.write(fh.read())
    wh.write(sh.read())
    wh.write(th.read())
    
    fh.close()
    sh.close()
    th.close()
    
    wh.close()

print("Finish read!")

data = ""
image = Image.new("RGB", (777 * 2, 777))
pix = image.load()

ii = 0
for r in range(1, 778):
    path = "/mnt/e/대회/yisf 본선/Misc/Broken_PNG_out/" + str(r) + ".png"
    img = Image.open(path)
    p = img.load()
    print("[" + path + "] width : " + str(img.size[0]) + " /  height : " + str(img.size[1]))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pix[ii * 2 + i, j] = p[i, j]
    ii += 1


image.save("/mnt/e/대회/yisf 본선/Misc/Broken_PNG.png", "PNG")
