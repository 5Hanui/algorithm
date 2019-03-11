#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int cache[100001];
int sum(int n) {
	int s = sqrt(n);
	int p = pow(s, 2);
	if (n == 1 || n == 0 || n == p) return 1;
	int &ret = cache[n];
	if (ret >=0 ) return ret;
	ret = 987654321;
	for (int i = s; i >= 1; i--) {
		ret = min(ret, sum(n - (i*i)) + 1);
	}
	return ret;

}
int main() {
	int num;
	cin >> num;
	memset(cache, -1, sizeof(cache));
	cout<<sum(num)<<endl;
	return 0;
}