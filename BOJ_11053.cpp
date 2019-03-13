#include <iostream>
#include <algorithm>
using namespace std;
int d[1001];
int a[1001];
int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> a[i];
	for (int i = 1; i <= n; i++) {
		d[i] = 1;
		for (int j = 0; j < i; j++) {
			if (a[i] > a[j] && d[i] < d[j] + 1)
				d[i] = d[j] + 1;
		}
	}
	int ans = 0;
	for (int i = 1; i <= n; i++)
		ans = max(ans,d[i]);
	cout << ans << endl;
	return 0;
}