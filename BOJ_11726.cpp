#include <iostream>
#include <cstring> 
using namespace std;
int cache[1001];
int tile(int n) {
	if (n == 1) return 1;
	if (n == 2) return 2;
	int &ret = cache[n];
	if (ret != -1) return ret;
	ret = 0;
	ret = tile(n - 1) + tile(n - 2);
	return ret%10007;
}
int main() {
	int num;
	cin >> num;
	if (num < 1 || num>1000) exit(-1);
	memset(cache, -1, sizeof(cache));
	cout << tile(num) << endl;
}