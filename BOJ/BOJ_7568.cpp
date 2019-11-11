#include<iostream>
#include<algorithm>
using namespace std;
pair<int, int> p[50];
int main() {
	int n;
	cin >> n;
	int rank[50] = { 0 };
	for (int i = 0; i < n; i++) {
		cin >> p[i].first >> p[i].second;
	}
	for (int i = 0; i < n-1; i++) {
		for (int j = i + 1; j < n; j++) {
			if ((p[i].first < p[j].first) && (p[i].second < p[j].second)) {
				rank[i] += 1;
			}
			else if ((p[i].first > p[j].first) && (p[i].second > p[j].second)) {
				rank[j] += 1;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		cout << rank[i]+1 <<" ";
	}
}