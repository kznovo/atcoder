#include <stdio.h>

int main(void)
{
	int n, y;
	scanf("%d %d", &n, &y);

	if ((n * 10000) < y)
	{
		printf("-1 -1 -1");
		return 0;
	}

	for (int a = 0; a <= n; ++a)
	{
		int ap, maxB;
		ap = 10000 * a;
		maxB = 5000 * (n - a);

		if (ap > y) break;
		if ((ap + maxB) < y) continue;

		for (int b = 0; b <= (n - a); ++b)
		{
			int bp, c, cp, tmp;
			bp = 5000 * b;
			
			if ((ap + bp) > y) break;

			c = n - a - b;
			cp = 1000 * c;
			tmp = ap + bp + cp;

			if (tmp > y) break;
			if (tmp == y)
			{
				printf("%d %d %d", a, b, c);
				return 0;
			}
		}
	}

	printf("-1 -1 -1");

	return 0;
}
