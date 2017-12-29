#include <stdio.h>
#include <stdlib.h>

int main(void){
	int a, b, c = 0;
	int temp;
	
	scanf("%d %d", &a, &b);
	
	if(a == b){
		c = 0;
	}else{
		if(a < b){
			temp = b - a;
		}else{
			temp = a - b;
		}
		while(temp){
			if(temp > 10){
				c += temp / 10;
				temp %= 10;
			}else if(temp > 5){
				if(temp >= 8){
					c += 1;
					temp = 10 - temp;
				}else{
					c += temp / 5;
					temp %= 5;
				}
			}else{
				if(temp >= 3){
					c += 1;
					temp = 5 - temp;
				}else{
					c += temp;
					break;
				}
			}
		}
	}
	
	printf("%d", c);
	return 0;
}
