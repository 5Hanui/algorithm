#include <iostream>
#include<cmath>
using namespace std;
int c[1000000];
int next(int n,int p) {
	int s = 0;
	while (n > 0) {
		s += pow(n % 10, p);
		n /= 10;
	}
	return s;
}
int length(int a,int p,int cnt) {
	if (c[a] != 0) //방문했다면
		return c[a] - 1;
	c[a] = cnt;
	int n = next(a,p);
	return length(n, p, cnt + 1);
}
int main() {
	int a, p;
	cin >> a >> p;
	int cnt = 1;
	cout << length(a, p, cnt) << endl;
	return 0;
}