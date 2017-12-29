#include <stdio.h>
#include <stdlib.h>

int arr[49][49];

int main(void){
	int i, j;
	int x, y;
	int num;
	
	scanf("%d", &num);
	
	x = num / 2;
	y = 0;
	
	for(i = 0 ; i < num * num ; i ++){
		arr[x][y] = i + 1;
		
		if(i != 0 && (i + 1) % num == 0){
			y++;
		}else{
			y--;
			x++;
		}
		
		if(y < 0)
			y = num - 1;
		if(x == num)
			x = 0;
	}
	
	for(j = 0 ; j < num ; j ++ ){
		for(i = 0 ; i < num ; i ++ ){
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
	return 0;
}
