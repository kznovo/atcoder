#include <stdio.h>

int main(void)
{
	int a, b, c, x, r;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	scanf("%d", &x);

	r = 0;
	int tmpa, tmpb, tmpc, tmpr;
	for (int ia = 0; ia <= a; ++ia)
	{
		tmpa = 500 * ia;
		if (tmpa > x) break;

		for (int ib = 0; ib <= b; ++ib)
		{
			tmpb = 100 * ib;
			if (tmpa + tmpb > x) break;

			for (int ic = 0; ic <= c; ++ic)
			{
				tmpc = 50 * ic;
				tmpr = tmpa + tmpb + tmpc;
				if (tmpr > x) break;
				if (tmpr == x) ++r;
			}
		}
	}

	printf("%d", r);
	return 0;
}
