#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>

std::map<int, int> m;
// 키는 데이터, 값은 순서량

int input[50000];

int main() {

	int n;
	
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", input + i);
	}

	for (int i = 0; i < n; i++) {
		m[input[i]] = 0;
	}

	int pri = 0;

	for (auto i = m.begin(); i != m.end(); i++) {
		i->second = pri++;
	}

	for (int i = 0; i < n; i++) {
		printf("%d ", m[input[i]]);
	}

	return 0;
}