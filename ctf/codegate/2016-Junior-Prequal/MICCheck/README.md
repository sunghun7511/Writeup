# Codegate 2016 Junior Prequal MICCheck
## Problem
This binary receive one input(%input%) and execute only one command.
```
/bin/ls -al /dev/%input%
```

However, some of these characters are filtered before this input is executed.

`'`, `&`, `;`, `|`, `"`, ` `

Unfortunately, we also cannot use environment variables.

## How to solve
The key to solve this problem is \`.

### Process
1. Execute binary and input \`sh\`.
2. Input `cat mic.flag.txt > output`
3. Input `Ctrl + c` to exit.
4. Read `output` file with some command like `cat`!
