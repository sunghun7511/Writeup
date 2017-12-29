#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int all = 0;
    int h, m, s, add;

    scanf("%d %d %d", &h, &m, &s);
    scanf("%d", &add);

    all += h * 60 * 60;
    all += m * 60;
    all += s;

    all += add;

    printf("%d %d %d", all / 60 / 60 % 24, all / 60 % 60, all % 60);
    
    return 0;
}