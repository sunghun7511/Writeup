#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n, i;
	long long int all = 0;

	scanf("%d", &n);

	for(i = 2 ; i <= n / 2 ; i ++){
		if(n % i == 0){
			if(n / i < i){
				break;
			}
			all += i;
			if(i != n / i)
				all += n / i;
		}
	}
	all += n + 1;

	printf("%lld", all);
	return 0;
}
