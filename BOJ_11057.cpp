#include <iostream>
using namespace std;
int d[1001][10];
int main() {
	int n;
	cin >> n;
	for (int i = 0; i <= 9; i++)
		d[1][i] = 1;
	for (int i = 2; i <= n; i++) {
		for (int k = 0; k <= 9; k++) {
			for (int l = 0; l <= k; l++) {
				d[i][k] += d[i - 1][l];
				d[i][k] %= 10007;
			}
		}
	}
	long long ans = 0;
	for (int i = 0; i <= 9; i++)
		ans += d[n][i];
	ans %= 10007;
	cout << ans << endl;
	return 0;
}