#include <iostream>
using namespace std;
int cache[101][10];
//cache[n][l] : 길이가 n이면서 끝자리가 l인 계단수
long long mod = 1000000000;
int main() {
	int n;
	cin >> n;
	for (int i = 1; i < 10; i++)
		cache[1][i] = 1; //*한자리이므로 1~9가능
	for (int i = 2; i <= n; i++) {
		for (int l = 0; l < 10; l++) {
			cache[i][l] = 0;
			if (l - 1 >= 0) cache[i][l] += cache[i - 1][l - 1]; //-1이 되는 경우 제거
			if (l + 1 <= 9) cache[i][l] += cache[i - 1][l + 1]; //10이 되는 경우 제거
			cache[i][l] %= mod;
		}
	}
	long long ans = 0;
	for (int i = 0; i <=9; i++) 
		ans += cache[n][i];
	
	ans%=mod;
	cout << ans << endl;
	return 0;
}