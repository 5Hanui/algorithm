#include <iostream>
#include <queue>
#include<algorithm>

using namespace std;
#define N 201
int d[N][N];
bool check[N][N];
int n, k;
int S, X, Y;
int xy[4][2] = { {0,1},{0,-1} ,{1,0}, {-1,0} };
typedef struct {
	int x;
	int y;
}Point;
vector<pair<int,Point>> virus;
void bfs() {
	int len = virus.size();
	for (int i = 0; i < len; i++) {
		Point p = { virus[i].second.x, virus[i].second.y };
		for (int j = 0; j < 4; j++) {
			Point next = { p.x + xy[j][0], p.y + xy[j][1] };
			if (next.x<1 || next.x>n || next.y<1 || next.y>n) continue;
			if (d[next.y][next.x] == 0) {
				d[next.y][next.x] = virus[i].first;
				Point tmp = { next.x, next.y };
				virus.push_back(make_pair(d[next.y][next.x], tmp));
			}
		}
	}
	virus.erase(virus.begin(), virus.begin() + len);
}
bool cmp(pair<int, Point>a, pair<int, Point>b) {
	return (a.first < b.first) ? true : false;
}
int main() {
	cin >> n >> k;
	for (int i = 1; i <=n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> d[i][j];
			if (d[i][j] != 0) {
				Point tmp = { j,i };
				virus.push_back(make_pair(d[i][j], tmp));
			}
		}
	}
	cin >> S >> X >> Y;
	sort(virus.begin(), virus.end(),cmp);
	for (int i = 0; i < S; i++) {
		bfs();
	}
	cout << d[X][Y] << endl;
}

