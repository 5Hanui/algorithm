#include <iostream>
#include <algorithm>
int d[10001][3]; //
int a[10001]; //Á¡¼ö
using namespace std;
int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n;i++) {
		cin >> a[i];
	}
	d[1][0] = 0, d[1][1] = a[1];
	for (int k = 2; k <= n; k++) {		
		d[k][0] = max(d[k - 1][0], max(d[k - 1][1], d[k - 1][2]));
		d[k][1] = d[k - 1][0] + a[k];
		d[k][2] = d[k - 1][1] + a[k];
	}
	int ans=0;
	for (int i = 1; i <= n; i++)
		ans = max(max(ans, d[i][0]), max(d[i][1], d[i][2]));
	cout << ans << endl;
	return 0;
}