#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool cmp(string a, string b) {
	if (a.length() != b.length())
		return a.length() < b.length();
	else if (a.length() == b.length()) {
		int sumA = 0, sumB = 0;
		for (int i = 0; i < a.length(); i++) {
			if (a[i] - '0' >= 0 && a[i] - '0' <= 10)
				sumA += a[i]-'0';
			if (b[i] - '0' >= 0 && b[i] - '0' <= 10)
				sumB += b[i]-'0';
		}
		if (sumA == sumB)
			return a < b; 
		else if (sumA != sumB)
			return sumA < sumB;
	}

	
	
}

int main() {
	int testcase;
	cin >> testcase;
	string str;
	vector<string> strArr;
	while (testcase--) {
		cin >> str;
		strArr.push_back(str);
	}
	sort(strArr.begin(), strArr.end(), cmp);
	for (int i = 0; i < strArr.size(); i++)
		cout << strArr[i] << endl;
	return 0;
}