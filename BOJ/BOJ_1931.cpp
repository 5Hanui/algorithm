#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector <pair<int, int>> p;
bool comp(const pair<int, int>& a, const pair<int, int>& b) {
	if (a.second == b.second)
		return a.first < b.first;
	return a.second < b.second;
}
int count() {
	int cnt = 1, time = 0;
	time += p[0].second;
	for (int i = 1; i < p.size(); i++) {
		if (p[i].first >= time) {
			time = p[i].second;
			cnt += 1;
		}
	}
	return cnt;
}
int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int start, stop;
		cin >> start >> stop;
		p.push_back(make_pair(start, stop));
	}
	sort(p.begin(), p.end(), comp);
	cout << count() << endl;
	return 0;
}
