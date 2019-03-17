#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	long long range = 1;
	int count = 1;
	long long t = 1;
	while (1) {
		if (range >= n)
			break;
		t = 6 * (count++);
		range += t;
	}
	cout << count << endl;
	return 0;
}