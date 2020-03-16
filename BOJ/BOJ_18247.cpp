#include <iostream>
using namespace std;
int T;
int N, M;
int L = 12;
int cinema(int n, int m) {
	if (n < L || m<4) return -1;
	if (n >= L) {
		return (L - 1) * m + 4;
	}
}
int main() {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		cout << cinema(N, M) << endl;
	}
}