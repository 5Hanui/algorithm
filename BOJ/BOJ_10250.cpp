#include <iostream>
using namespace std;
int acmHotel(int h, int w, int n) {
	int roomNum;
	int y, x;
	y = n%h;
	if (y!=0) x = n / h + 1;
	if (y == 0) {
		y = h;
		x = n / h;
	}
	roomNum = 100 * y + x;
	return roomNum;
}
int main() {
	int test;
	cin >> test;
	while (test--) {
		int h, w, n;
		cin >> h >> w >> n;
		cout << acmHotel(h, w, n) << endl;
	}
	
	return 0;
}
