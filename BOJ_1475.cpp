#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int n;
	int c[10] = { 0 };
	cin >> n;
	while (1) {
		c[n % 10]++;
		if (n / 10 == 0) break;
		n /= 10;
	}
	int m = 0;
	int num = (c[6] + c[9] + 1) / 2;
	for (int i = 0; i <= 9; i++) {
		if(i!=6 && i!=9) m = max(m, c[i]);
	}
	cout << max(m,num) << endl;
	return 0;
}