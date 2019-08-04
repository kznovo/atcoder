#include <stdio.h>
#include <string.h>

int main(void)
{
	int n;
	scanf("%d", &n);

	int r;
	for (int i = 0; i < n; ++i)
	{
		int a;
		scanf("%d", &a);
		int tmp = 0;

		while (a % 2 == 0)
		{
			a /= 2;
			++tmp;
		}

		if (i == 0  | tmp == 0)
		{
			r = tmp;
			continue;
		}
		
		if (tmp < r) r = tmp;
	}
	
	printf("%d", r);
	return 0;
}


