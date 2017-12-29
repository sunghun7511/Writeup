#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int a, b, c;
	int temp;
    
    scanf("%d %d %d", &a, &b, &c);
	
	while (b){
        temp = a % b;
        a = b;
        b = temp;
    }
    
	while (c){
        temp = a % c;
        a = c;
        c = temp;
    }
    
    printf("%d", a);
	return 0;
}
