# Ubuntu-ctf misc How to r3c0v3ry
## Prob
### How to r3c0v3ry?  ( 830p )
file recovery

https://drive.google.com/open?id=0B6fyAu3JzK2ccG8xejJpcVFPbjQ
## How to solve
1. reverse all data with this source
```python
fp = open("thisflag", "rb")

reads = fp.read()[::-1]

fp.close()

fp2 = open("output.png", "wb")
fp2.write(reads)
fp2.close()
```
2. change header

From
```
00 00 00 00 0D 0A 1A 0A 00 00 00 0D 49 48 44 52     ............IHDR
```
To
```
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52     ‰PNG........IHDR
```

## Flag
![](output.png)