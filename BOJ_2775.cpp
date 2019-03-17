#include <iostream>
using namespace std;
int main() {
	int t;
	int p[15][15] = { 0 };
	for (int i = 1; i <= 14; i++) {
		p[i][1] = 1, p[0][i] = i;
	}
	for (int k = 1; k <= 14; k++) {
		for (int j = 2; j <= 14; j++) {
			p[k][j] = p[k - 1][j] + p[k][j - 1];
		}
	}
	cin >> t;
	while (t--) {
		int n, k;
		cin >> n;
		cin >> k;
		cout << p[n][k] << endl;
	}
	return 0;
}