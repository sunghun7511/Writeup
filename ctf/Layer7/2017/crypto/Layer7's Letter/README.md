# Layer7 CTF 2017 crypto Layer7's Letter

## Overview
The problem gives me the file `letter_21a086d3e3b75772f056e96e6dcbe1fd`.<br />
The file contains encrypted text.

Maybe it was encrypted by `caesar cipher`.

## How to solve
I use `python` language.

```python
MAX_ROT = 26

class Rotator:
    def __init__(self):
        pass
    
    def isValid(self, n):
        return n.isalpha() # or blabla..

    def find(self, n, amt = 1):
        rot = self._rotate(n, amt)
        return rot if self.isValid(rot) else self.find(n, amt+1)

    def find(self, n, findstr, amt = 1):
        rot = self._rotate(n, amt)
        return rot if findstr in rot else self.find(n, findstr, amt+1)
    
    def _rotate(self, n, amt):
        output = ""
        for ind, c in enumerate(n):
            if not c.isalpha():
                output = output + c
                continue
            key = 'A' if c.isupper() else 'a'
            output = output + chr((ord(c) - ord(key) + amt) % MAX_ROT + ord(key))
        return output

if __name__ == "__main__":
    f = open("letter_21a086d3e3b75772f056e96e6dcbe1fd")
    encrypted = f.read()
    f.close()

    rot = Rotator()
    print rot.find(encrypted, "flag")
```

## Flag
I can find flag after run this python code.
This is output of code.
```
Late7 has been with the school since 2001, when Sunlin Internet High School was designated as the first IT characteristic high school in Seoul. Students who are interested
in security are building a club, and in the rare areas of hacking, each other has helped each other and has studied security. The systematic curriculum and the passion of the club members and the sense of responsibility have contributed to the history of 17 years. The World War Tennis Championships, hosted by the World's Most Wanted by Death
and Defense Ministry, are published in various fields, including the International Hacking Conference, organized by the International Hacking Conference, and publishing in
various fields, including computers, Web portals, and embedded formats. Today we have hidden a flag. FLAG{Layer7_is_gooddddddddd}
```

Flag is `FLAG{Layer7_is_gooddddddddd}`.