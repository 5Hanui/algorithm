#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<int> a[20001];
int check[20001];
void dfs(int node,int e) {
	check[node] = e;
	for (int i = 0; i < a[node].size(); i++) {
		int next = a[node][i];
		if (check[next] == false) {
			dfs(next,3-e);
		}
	}
}
int main() {
	int test;
	cin >> test;
	while (test--) {
		int n, m;
		cin >> n >> m;
		for (int i = 1; i <= n; i++) {
			a[i].clear();
			check[i] = 0;
		}
		for (int i = 0; i < m; i++) {
			int u, v;
			cin >> u >> v;
			a[u].push_back(v);
			a[v].push_back(u);
		}
		for (int i = 1; i <= n; i++) {
			if (check[i] == 0)
				dfs(i, 1);
		}
		bool ok = true;
		for (int i = 1; i <= n; i++) {
			for (int k = 0; k < a[i].size(); k++) {
				int y = a[i][k];
				if (check[y] == check[i])
					ok = false;
			}
		}
		string s= (ok == true) ? "YES" : "NO";
		cout << s << endl;
		
	}
	return 0;
}