#include <stdio.h>
#include <stdlib.h>

char arr[100][100];

int custom_min(int a, int b){
	return a > b ? b : a;
}

int custom_max(int a, int b){
	return a > b ? a : b;
}

int main(void) {
	int i, x, y, tx, ty, ttx, tty;
	int all = 0;
	
	for(i = 0 ; i < 4 ; i ++ ){
		scanf("%d %d %d %d", &tx, &ty, &ttx, &tty);
		
		for(x = custom_min(tx, ttx) ; x < custom_max(tx, ttx) ; x ++){
			for(y = custom_min(ty, tty) ; y < custom_max(ty, tty) ; y ++){
				arr[x][y] = 1;
			}
		}
	}
	
	for(x = 0 ; x < 100 ; x ++){
		for(y = 0 ; y < 100 ; y ++){
			all += arr[x][y];
		}
	}
	
	printf("%d", all);
	
	return 0;
}
