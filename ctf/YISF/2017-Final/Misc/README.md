# YISF 2017 Final MISC Broken_PNG
## Overview
The problem gives me a file what named `[MISC] Broken_PNG.7z`.

If you unzip that archive file, you can see many sliced folders. <br />
Folders are x axis and files are datas.

But, files are also sliced and file order is random.<br />
Haha, don't worry. file format is `png`.

File signature is `89 50` and End Of File is `60 82`. (hex value)

After that, just merge image files!

## How to solve
To solve this problem, you need programming.

I use `python` & python image library `PIL`.
```python
import os, sys
from PIL import Image

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

for f1 in os.listdir("./Broken_PNG/"):
    first = ""
    second = ""
    third = ""
    for f2 in os.listdir("./Broken_PNG/" + f1):
        path = "./Broken_PNG/" + f1 + "/" + f2
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

    path = "./Broken_PNG_out/" + f1 + ".png"
    
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
    path = "./Broken_PNG_out/" + str(r) + ".png"
    img = Image.open(path)
    p = img.load()
    print("[" + path + "] width : " + str(img.size[0]) + " /  height : " + str(img.size[1]))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pix[ii * 2 + i, j] = p[i, j]
    ii += 1


image.save("./Broken_PNG.png", "PNG")

```

## Flag
![Flag](./Broken_PNG.png)