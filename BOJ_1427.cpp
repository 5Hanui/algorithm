#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	int n;
	cin >> n;
	vector<int> arr;
	while (1) {
		if (n < 10) {
			arr.push_back(n);
			break;
		}
		int a = n % 10;
		arr.push_back(a);
		n /= 10;
	}
	sort(arr.begin(), arr.end());
	for (int i = arr.size()-1; i >=0; i--) {
		cout << arr[i];
	}
	cout << endl;
	return 0;
}