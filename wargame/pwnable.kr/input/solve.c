#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <sys/socket.h>
#include <arpa/inet.h>


#define BUF_SIZE 4096

int main(int argc, char ** argv){

    char *arr[] = {"/home/input2/input", [1 ... 99] = "A", 0};
    char *env[] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe", 0};
    int in[2], err[2];

    int soc;
    struct sockaddr_in addr;

    FILE *st4;
    
    // for stage 1
    arr['A'] = "\x00";
    arr['B'] = "\x20\x0a\x0d";

    // for set port (will use in stage 5)
    arr['C'] = "10001";

    // for stage 4
    st4 = fopen("\x0a", "w");
    fwrite("\x00\x00\x00\x00", 1, 4, st4);
    fclose(st4);


    pipe(in);
    pipe(err);

    if(!fork()){
        close(in[0]);
        close(err[0]);

        write(in[1], "\x00\x0a\x00\xff", 4);
        write(err[1], "\x00\x0a\x02\xff", 4);

    }else{
        close(in[1]);
        close(err[1]);
        
        dup2(in[0], 0);
        dup2(err[0], 2);
        
        close(in[0]);
        close(err[0]);

        execve("/home/input2/input", arr, env);

        perror("Fail to execute input..");
        exit(EXIT_FAILURE);
    }

    soc = socket(AF_INET, SOCK_STREAM, 0);

    if(soc == -1){
        perror("socket create failed..");
        exit(EXIT_FAILURE);
    }
    
    memset(&addr, 0, sizeof(addr));

    addr.sin_family = AF_INET;
    addr.sin_port = htons(10001);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if(connect(soc, (struct sockaddr*)&addr, sizeof(addr)) == -1){
        perror("socket connect failed..");
        exit(EXIT_FAILURE);
    }

    write(soc, "\xde\xad\xbe\xef", 4);
    close(soc);
    
    printf("Success!\n");
    return 0;
}