#include<stdio.h>
#include<stdlib.h>

int main(){
    int fd;

    printf("test_1\n");

    fd=open("/dev/urandom",0);

    dup2(fd,1);

    printf("test_2\n");
    fd=2;
    dup2(fd,1);
    printf("test_3\n");

    return 0;
}
