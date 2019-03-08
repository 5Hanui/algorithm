#include<iostream>
using namespace std;
int main() {
	int test;
	cin >> test;
	int d[11];
	d[0]=0, d[1] = 1, d[2] = 2, d[3]=4;
	for (int i = 4; i < 11; i++) {
		d[i] = d[i - 1] + d[i - 2] + d[i - 3];
	}
	while (test--) {
		int num;
		cin >> num;
		cout << d[num] << endl;
	}
	return 0;
}