#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);

	int t[n], x[n], y[n];
	for (int i = 0; i < n; ++i) scanf("%d %d %d", &t[i], &x[i], &y[i]);
	
	int pt, px, py;
	pt = t[0];
	px = x[0];
	py = y[0];

	if (pt < (px + py) | ((pt % 2) + (px % 2) + (py % 2)) % 2)
	{
		printf("No");
		return 0;
	}

	int it, ix, iy, mt, mx, my;
	for (int j = 1; j < n; ++j)
	{
		it = t[j];
		ix = x[j];
		iy = y[j];

		mt = it - pt;
		mx = ix - px;
		my = iy - py;

		
		if (mt < (mx + my) | ((mt % 2) + (mx % 2) + (my % 2)) % 2)
		{
			printf("No");
			return 0;
		}

		pt = mt;
		px = mx;
		py = my;
	}

	printf("Yes");
	return 0;
}

