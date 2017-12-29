#include <stdio.h>
#include <stdlib.h>

int main(void){
	/*
	* 못풀었슴다.
	*/

	int i, j, n, delta, tmpi, tmpj;
	int max = -2000000000;
	int arr[100000] = {0, };
	
	scanf("%d %d", &n, &delta);
	
	for(i = 0 ; i < n ; i ++ ){
		scanf("%d", &j);
		
		if(i >= delta){
			tmpi = i % delta;
			if(max < arr[tmpi]){
				max = arr[tmpi];
			}
			arr[tmpi] = 0;
			for(tmpj = 0 ; tmpj < delta ; tmpj ++){
				arr[tmpj] += j;
			}
		}else{
			for(tmpi = delta - 1 ; tmpi >= 0 ; tmpi --){
				arr[tmpi] += j;
			}
		}
	}
	tmpi = i % delta;
	if(max < arr[tmpi]){
		max = arr[tmpi];
	}
	
	printf("%d", max);
	return 0;
}
