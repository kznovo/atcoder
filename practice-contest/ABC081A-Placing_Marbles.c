#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char str[4];
	int i;
	scanf("%s", str);
	sscanf(str, "%d", &i);
	printf("%d", (i/100%10) + (i/10%10) + (i%10));
	return 0;
}
