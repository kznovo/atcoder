#include <stdio.h>

int main(void)
{
	int n, a, b, i, r;
	scanf("%d %d %d", &n, &a, &b);
	r = 0;

	for (i = 1; i <= n; ++i)
	{
		int x1 = i % 10;
		int x2 = i / 10 % 10;
		int x3 = i / 100 % 10;
		int x4 = i / 1000 % 10;
		int x5 = i / 10000 % 10;
		int x = x1 + x2 + x3 + x4 + x5;
		if (a <= x & x <= b) r += i;
	}

	printf("%d", r);

	return 0;
}
