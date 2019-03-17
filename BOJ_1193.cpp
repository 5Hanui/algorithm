#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	long long range1 = 1;
	long long range2 = 1;
	int cnt = 1;
	while (1) {
		if (range2 >= n && range1 <= n) {
			if (cnt % 2 == 0) {
				cout << n - range1 + 1 << "/" << cnt - n + range1 << endl;
			}
			if (cnt % 2 == 1) {
				cout << cnt - n + range1 << "/" << n - range1 + 1 << endl;
			}
			break;
		}
		range1 += cnt;
		cnt++;
		range2 +=cnt;
	}
}