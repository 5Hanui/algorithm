#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
#define MAX 26
int d[MAX][MAX];
bool check[MAX][MAX];
int xy[4][2] = { { 0, 1 },{ 0, -1 },{ 1, 0 },{ -1, 0 } };
int ans[MAX];
int n;
typedef struct {
	int x;
	int y;
}Point;

int bfs(int y, int x) {
	queue<Point> q;
	q.push({ x, y });
	check[y][x] = true;
	int cnt = 0;
	while (!q.empty()) {
		cnt++;
		Point p = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			Point next = { p.x + xy[i][0] , p.y + xy[i][1] };
			if (next.x < 0 || next.x >= n || next.y < 0 || next.y >= n) continue;
			if (d[next.y][next.x] == 1 && check[next.y][next.x] == false) {
				q.push(next);
				check[next.y][next.x] = true;
			}
		}
	}

	return cnt;
}

int main() {
	cin >> n;
	char xy;
	vector<int> v;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> xy;
			d[i][j] = xy - '0';
		}
	}
	int l=0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (d[i][j] == 1 && check[i][j] == false) {
				l = bfs(i, j);
				v.push_back(l);
			}
		}
	}
	sort(v.begin(), v.end());
	cout << v.size() << endl;
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << endl;
	}


	return 0;

}