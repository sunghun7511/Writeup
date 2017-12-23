/*
* 
* 보지마요 못풀었으니까..
* 
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int main(void){
    // int v10;
    char Str[] = {0x49, 0x72, 0x5B, 0x47, 0x7B, 0x6D, 0x7F};
    char main_k2[4];
    int32_t main_k2_2;
    char FLAG[] = "FLAG";
    int i, j;
    int isDebugger;

    int v4;
    int v5;
    int v6;
    int v7;

    v4 = 34;
    v5 = 42;
    v6 = 54;
    v7 = 33;

    // *(int *)Str = 0x475B7249;
    // v10 = 0x7B6D7F;
    *(int *)main_k2 = 0x466F6964;
    main_k2_2 = 0x6569;

    int after7[] = {1, 22, 51, 34, 22, 43, 12, 34, 37, 54, 28};

    for(i = 0 ; i < strlen(Str) ; i ++){

        // subroutine5
        {
            for(j = 0 ; j < strlen(FLAG) ; j ++){
                printf("%c", FLAG[j]);
            }
            printf("%c", 123);
            
            // subroutine7
            {
                isDebugger = 4;
                after7[0 + isDebugger] = isDebugger;

                for(j = 0 ; j < strlen(Str) ; j ++){
                    printf("%c", (j * j ^ Str[j]) ^ after7[j]);
                }

                // subroutine9
                {
                    isDebugger = 0;
                    *(&v4 + isDebugger) = after7[8];
                    *(&v4 + 3 * isDebugger) = after7[10];
                    for (j = 0; j < strlen(Str); ++j) {
                        printf("%c", (j * j ^ main_k2[j]) ^ *(&v4 + 4 * j));
                    }
                }
            }
            printf("%c\n", 125);
        }
        printf("%c", i * i ^ Str[i]);
    }
    puts("");
    return 0;
}