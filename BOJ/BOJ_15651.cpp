#include <iostream>
#include <vector>
using namespace std;
int N, M;
vector<int> d;
void dfs(int cnt) {
	if (cnt == M) {
		for (int i = 0; i < M; i++)
			cout << d[i] << " ";
		cout << "\n";
		return;
	}
	for (int j = 1; j <= N; j++) {
		d.push_back(j);
		dfs(cnt + 1);
		d.pop_back();
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		d.push_back(i);
		dfs(1);
		d.pop_back();
	}
	return 0;
}