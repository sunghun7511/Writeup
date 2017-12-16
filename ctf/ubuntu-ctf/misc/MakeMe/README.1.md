# Ubuntu-ctf misc MakeMe
## Prob
### MakeME
Give to me some file that named as `flag.txt`

## What I think?
The `flag.txt` file is composed of any text that have a pattern.
like this
```
(0, 0, 0)
(255, 255, 255)
```
Hmm.. It looks like `tuple in python` & `RGB Color value`!

## How to solve
1. Let's make a script!
```python
import os, sys
from ast import literal_eval
from PIL import Image


fp = open("flag.txt", "r")

image = Image.new("RGB", (631, 193))
pix = image.load()

i = 0
j = 0
while True:
    line = fp.readline()
    if not line: break
    tup = literal_eval(line)
    pix[i, j] = tup
    if i == 630:
        i = 0
        j = j + 1
        print(j)
    else:
        i = i + 1

image.save("./outout.png", "PNG")

fp.close()
```
2. Then, run the script!

## Flag
![](outout.png)