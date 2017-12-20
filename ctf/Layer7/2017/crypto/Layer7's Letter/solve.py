MAX_ROT = 26

class Rotator:
    def __init__(self):
        pass
    
    def isValid(self, n):
        return n.isalpha()

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