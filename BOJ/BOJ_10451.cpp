#include<iostream>
#include<cstdio>
using namespace std;
int a[1001];
int c[1001];
void dfs(int node) {
	if (c[node]) return;
	c[node] = true;
	dfs(a[node]);
}
int main() {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		for (int i = 1; i <= n; i++) {
			cin >> a[i];
			c[i] = false;
		}
		int ans = 0;
		for (int k = 1; k <= n; k++) {
			if (c[k] == false) {
				dfs(k);
				ans += 1;
			}

		}
		cout << ans << endl;
	}
	return 0;
}
