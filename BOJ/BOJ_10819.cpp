#include<iostream>
#include<vector>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int sumArr(vector<int> arr) {
	int sum = 0;
	for (int i = 0; i < arr.size()-1; i++) {
		sum += abs(arr[i] - arr[i + 1]);
	}
	return sum;
}
int main() {
	int n, num;
	vector<int> v;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		v.push_back(num);
	}
	int max = 0;
	sort(v.begin(), v.end());
	do {
		int sum = sumArr(v);
		max = (sum > max) ? sum : max;
	} while (next_permutation(v.begin(), v.end()));
	cout << max << endl;
	return 0;
}