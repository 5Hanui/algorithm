#include <iostream>
using namespace std;
int d[10001];
int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int s;
		scanf("%d",&s);
		d[s]++;
	}
	for (int i = 1; i < 10001; i++) {
		for (int j = 0; j < d[i]; j++)
			printf("%d\n",i);
	}
	return 0;
}