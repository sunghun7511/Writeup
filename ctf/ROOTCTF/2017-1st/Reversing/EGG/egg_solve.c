#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char f[] = "Mh;y;mR1@OijQhHW6Ah=hB";
int y = 17;
int m = 12;
int d = 21;

int r(int a){
    int i, j, k;
    for(i = 0 ; i < y ; i ++){
        a ^= y;
        for(j = 0 ; j < m ; j ++){
            a ^= m;
            for(k = 0 ; k < d ; k ++){
                a ^= d;
            }
        }
    }
    return a;
}

long long int sha(int a){
    int as[] = {8, 9, 15, 5, 11, 1, 3, 5, 13, 1, 14, 3, 4, 14, 7, 4, 193, 6, 6, 12, 15, 10, 12, 10, 2, 13, 8, 7, 3, 7, 1, 7, 5, 8, 12, 3, 4, 11, 14, 5, 1, 11, 0, 3, 9, 4, 5, 6, 8, 12, 5, 3, 10, 15, 3, 14, 15, 4, 8, 10, 11, 15, 2};
    return (unsigned int)as[(signed int)r(a)];
}

int main(void){
    int i = 0;

    for ( i = 0; i < strlen(f); ++i )
        f[i] ^= sha(i + 2);
    
    printf("%s\n", f);
    return 0;
}