#include <iostream>
#include <queue>
#include <string.h>

using namespace std;
#define M 51
#define N 51
bool check[M][N];
int d[M][N];
int xy[4][2] = { {0,1}, {0,-1}, {1, 0}, {-1, 0} };
int m, n;
typedef struct{
	int x;
	int y;
}Point;
void bfs(int y, int x) {
	check[y][x] = true;
	queue<Point> q;
	q.push({ x, y });
	while (!q.empty()) {
		Point p = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			Point next = { p.x + xy[i][0], p.y + xy[i][1] };
			if (next.x < 0 || next.x >= m || next.y < 0 || next.y >= n) continue;
			if (check[next.y][next.x] == false && d[next.y][next.x] == 1) {
				check[next.y][next.x] = true;
				q.push({ next.x, next.y });
			}
		}
	}


}
int main() {
	int testcase, k;
	cin >> testcase;
	for (int i = 0; i < testcase; i++) {
		cin >> m >> n >> k;
		memset(check, false, sizeof(check));
		memset(d, 0, sizeof(d));
		for (int i = 0; i < k; i++) {
			int x, y;
			cin >> x >> y;
			d[y][x] = 1;
		}
		int component=0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (d[i][j] == 1 && check[i][j] == false) {
					bfs(i, j);
					component+=1;
				}
			}
		}
		cout << component << endl;
	}
}