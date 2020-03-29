#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N, M;
vector<long long> A;
int binarySearch(int left, int right, long long i) {
	while (left <= right) {
		int mid = (left + right) / 2;
		if (A[mid] == i) {
			return 1;
		}
		else if (A[mid] > i) {
			right = mid - 1;
		}
		else if (A[mid] < i) {
			left = mid + 1;
		}
	}
	return 0;
	
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; i++) {
		long long n;
		cin >> n;
		A.push_back(n);
	}
	sort(A.begin(), A.end());
	cin >> M;
	for (int i = 0; i < M; i++) {
		long long m;
		cin >> m;
		cout<< binarySearch(0,A.size()-1,m) <<'\n';
	}
	return 0;
}