#include <stdio.h>
#include <stdlib.h>

FILE *fp;

void sub_104C(int * a1, int a2) {
    int i; // [rsp+18h] [rbp-8h]
    int v4; // [rsp+1Ch] [rbp-4h]

    for ( i = a2 - 1; i >= 0; --i ) {
        v4 = rand() % a2;
        fprintf(fp, "%d\n", v4);
        printf("rand : %d\n", v4);
        if ( i != v4 ) {
            // Just swap with xor
            *(int *)(4LL * i + a1) ^= *(int *)(4LL * v4 + a1);
            *(int *)(4LL * v4 + a1) ^= *(int *)(4LL * i + a1);
            *(int *)(4LL * i + a1) ^= *(int *)(4LL * v4 + a1);
        }
    }
}
int main(int argc, char * argv){
    int i, j, l, k, m, tmp;
    int input[16] = {0, };
    int v9[128] = {0, };
    int output[128] = {1, };

    const int v8 = 16;

    fp = fopen("rand_data", "w");

    for ( i = 0; i < v8; ++i ) {
        for ( j = 8 * i; j < 8 * (i + 1); ++j ) {
            v9[j] = input[i] & 1;
            input[i] >>= 1;
        }
    }
    printf("debug\n");
    for ( k = 0; k <= 15; ++k ) {
        tmp = 1;
        for ( l = 0; l < 8 * v8; ++l ) {
            if ( v9[l] )
                tmp ^= 1u;
            v9[l] = tmp;
        }
        sub_104C(v9, 8 * v8);
    }
    fclose(fp);

    for ( m = 0; m <= 128; ++m ) {
        if ( v9[m] != output[m] ){
            printf("wrong..[%d]\n", m);
        }
    }

    /*
    for ( k = 0; k <= 15; ++k ) {
        tmp = 1;
        for ( l = 0; l < 8 * v8; ++l ) {
            if ( v9[l] )
                tmp ^= 1u;
            v9[l] = tmp;
        }
        sub_104C(v9, (unsigned int)(8 * v8));
    }

    for ( i = 0; i < v8; ++i ) {
        for ( j = 8 * i; j < 8 * (i + 1); ++j ) {
            output[i] |= (finals[j] << (j % 8));
        }
    }*/
    return 0;
}