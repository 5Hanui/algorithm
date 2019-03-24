#include <iostream>
#include <algorithm>
using namespace std;
long long a[100001][2];
long long d[100001][3];
long long sticker(int len) {
	d[1][0] = 0, d[1][1] = a[1][0], d[1][2] = a[1][1];
	int m = 0;
	for (int i = 2; i <= len; i++) {
		d[i][0] = max(d[i - 1][0], max(d[i - 1][1], d[i - 1][2]));
		d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[i][0];
		d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[i][1];
	}
	long long ans = 0;
	for (int i = 1; i <= len; i++) {
		ans = max(max(ans, d[i][0]), max(d[i][1], d[i][2]));
	}
	return ans;
}
int main() {
	int test;
	cin >> test;
	while (test--) {
		int len;
		cin >> len;
		for (int i = 1; i <= len; i++) {
			cin >> a[i][0];
		}
		for (int i = 1; i <= len; i++) {
			cin >> a[i][1];
		}
		cout << sticker(len)<<endl;
	}
	return 0;
}
