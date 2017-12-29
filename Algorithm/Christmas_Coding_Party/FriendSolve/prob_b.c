#include <stdio.h>

int main(void) {

	int sec; // = 86401;

	int valuehour = 0;
	int valuemin = 0;
	int valuesec = 0;

	int cooktime;

	scanf("%d %d %d %d", &valuehour, &valuemin, &valuesec, &cooktime);

	const int hour = 3600;
	const int min = 60;

	int valuesec_ = valuehour * 3600 + valuemin * 60 + valuesec;
	valuesec_ += cooktime;

	valuehour = valuemin = valuesec = 0;

	while (true) {
		if (valuesec_ - hour >= 0) {
			valuesec_ -= hour;
			valuehour++;
		} else {
			break;
		}
	}

	while (true) {
		if (valuesec_ - min >= 0) {
			valuesec_ -= min;
			valuemin++;
		} else {
			break;
		}
	}

	valuesec = valuesec_;

	printf("%d %d %d\n", valuehour % 24, valuemin % 60, valuesec % 60);

	return 0;
}
