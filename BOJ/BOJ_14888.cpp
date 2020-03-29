#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;
int cnt = 0;
int cNum = 0;
int N;
vector<int> A;
vector<int> total;
int check[4] = { 0 };
char op[4] = { '+','-','*','/' };
int calc(int x, int y, int idx) {
	int res = 0;
	if (idx == 0) {
		res = x + y;
	}
	else if (idx == 1) {
		res = x - y;
	}
	else if (idx == 2) {
		res = x * y;
	}
	else if (idx == 3) {
		y = (y < 0) ? y*(-1) : y;
		res = x / y;
	}
	return res;
}
void dfs(int cnt, int res) {
	if (cnt == cNum) {
		total.push_back(res);
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (check[i] != 0) {
			check[i] -= 1;
			int nRes = calc(res, A[cnt+1], i);
			dfs(cnt+1, nRes);
			check[i] += 1;
		}
	}

}
int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int n;
		cin >> n;
		A.push_back(n);
	}
	for (int i = 0; i < 4; i++) {
		int c;
		cin >> c;
		cNum += c;
		check[i] = c;
	}
	for (int i = 0; i < 4; i++) {
		if (check[i] != 0) {
			check[i] -= 1;
			int res = calc(A[0], A[1], i);
			dfs(1, res);
			check[i] += 1;
		}
	}
	sort(total.rbegin(), total.rend());
	cout << total[0] << endl;
	cout << total[total.size() - 1] << endl;


}