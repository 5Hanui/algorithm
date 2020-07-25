#include<iostream>
#include<queue>
#include<string.h>
#include<vector>
#define MAX 51
using namespace std;
int d[MAX][MAX];
bool visit[MAX][MAX];
typedef struct {
	int x;
	int y;
}Point;
vector<Point> list;
int w, h;
int xy[8][2] = { {-1, 0}, { 1, 0 }, { 0, -1 }, { 0, 1 } 
			,{ -1, -1 } ,{ 1, 1 },{ -1, 1 },{ 1, -1 } };
void bfs(int x, int y) {
	queue<Point> q;
	q.push({ x,y });
	visit[y][x] = true;
	while (!q.empty()) {
		Point p = q.front();
		q.pop();
		for (int i = 0; i < 8; i++) {
			Point next = { p.x + xy[i][0], p.y + xy[i][1] };
			if (next.x<0 || next.x>=w || next.y<0 || next.y>=h) continue;
			if (visit[next.y][next.x] == false && d[next.y][next.x] == 1) {
				visit[next.y][next.x] = true;
				q.push({ next.x, next.y });
			}
		}
	}

}
int main() {
	//int w, h;
	int n;
	int cnt = 0;
	queue<Point> empty;
	while (true) {
		cin >> w >> h;
		if (w == 0 && h == 0) break;
		list.clear();
		memset(d, 0, sizeof(d));
		memset(visit, false, sizeof(visit));
		cnt = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> n;
				d[i][j] = n;
				if (n == 1) list.push_back({ j, i });
			}
		}

		if (list.size() == 0) {
			cout << 0 << endl;
			continue;
		}
		for (int i = 0; i < list.size(); i++) {
			Point cur = list[i];
			if (visit[cur.y][cur.x] == false) {
				bfs(cur.x, cur.y);
				cnt++;
			}
		}
		cout << cnt << endl;
	}
	return 0;

}