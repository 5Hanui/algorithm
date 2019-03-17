#include <iostream>
#include <string>
using namespace std;
int main() {
	int m[12] = { 0, 31,28,31,30,31,30,31,31,30,31,30};
	string w[7] = { "SUN","MON","TUE","WED","THU","FRI","SAT"};
	int x, y;
	cin >> x >> y;
	int d = 0;
	d+=y;
	for (int i = 0; i < x; i++) {
		d += m[i];
	}
	cout << w[d % 7] << endl;
	return 0;

}