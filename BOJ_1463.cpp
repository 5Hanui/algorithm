#include <iostream>
#include <algorithm>
using namespace std;
int cache[1000001];
int makeOne(int n) {
	if (n == 1) return 0;
	if (cache[n]>0) return cache[n];
	cache[n] = makeOne(n - 1) + 1;
	if (n % 2 == 0) {
		int temp = makeOne(n / 2) + 1;
		if (cache[n] > temp) cache[n] = temp;
	}
	if (n % 3 == 0) {
		int temp = makeOne(n / 3) + 1;
		if (cache[n] > temp) cache[n] = temp;
	}
	return cache[n];
}
int main() {
	int num;
	cin >> num;
	cout << makeOne(num) << endl;
	return 0;
}