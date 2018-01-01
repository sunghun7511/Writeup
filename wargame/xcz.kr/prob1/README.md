# xcz.kr problem 1

## Overview

Title : End Of Image

Description : 
![](whysoserious.png)

## How to solve

Open with `Hex Editor`.

![](Hex.PNG)

This file is `PNG` File. <br />

But,

![](Hex2.PNG)

File footer is `FF D9`.<br />
`FF D9` is `JPG` file footer signature..

So, Let's find `FF D8` and copy after datas include `FF D8`.

![](Hex3.PNG)

![](Hex4.PNG)

![](Hex5.PNG)

Finally, I can see flag.

![](output.jpg)

# Flag

`JOg-dragonKER`