#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n;
	cin >> n;
	vector<int> arr(0, n);
	for (int i = 0; i < n; i++) {
		int s;
		scanf("%d",&s);
		arr.push_back(s);
	}
	sort(arr.begin(), arr.end());
	for (int i = 0; i < n; i++)
		printf("%d\n",arr[i]);
	return 0;
}