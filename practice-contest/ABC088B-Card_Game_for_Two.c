#include <stdio.h>


void Swap(int *a, int *b)
{
	int t = *a;
	*a = *b;
	*b = t;
}


int Partition(int arr[], int low, int high)
{
	int pivot = arr[high];
	int i = (low - 1);

	for (int j = low; j <= high - 1; ++j)
	{
		if (arr[j] <= pivot)
		{
			++i;
			Swap(&arr[i], &arr[j]);
		}
	}
	Swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}


void InnerQuickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		int pi = Partition(arr, low, high);
		InnerQuickSort(arr, low, pi - 1);
		InnerQuickSort(arr, pi + 1, high);
	}
}


void QuickSort(int arr[], int n)
{
	InnerQuickSort(arr, 0, n - 1);
}


int main(void)
{
	int n;
	scanf("%d", &n);

	int a[n];
	for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
	
	QuickSort(a, n);

	int rem, j, alice, bob, r;
	rem = n % 2;
	r = 0;
	for (j = rem; j < (n - rem); j += 2)
	{
		alice = a[j + 1];
		bob = a[j];
		r += alice - bob;
	}
	if (rem) r += a[0];

	printf("%d", r);

	return 0;
}
