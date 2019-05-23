#include <iostream>
using namespace std;
int coin[10];
int minNum(int n, int k) {
	int cnt = 0;
	for (int i = n - 1; i >= 0; i--) {
		if (coin[i] <= k) {
			int d = 0;
			d=k / coin[i];
			cnt += d;
			k = k - (d*coin[i]);
		}
	}
	return cnt;
}
int main() {
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		cin >> coin[i];
	cout << minNum(n, k) << endl;
}
