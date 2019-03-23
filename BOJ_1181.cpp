#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
bool sortWord(string & a, string & b) {
	if (a.length() != b.length()) {
		return a.length() < b.length();
	}
	else if (a.length() == b.length()) {
		return a < b;
	}
	
}
int main() {
	vector<string> dic;
	string str;
	int n;
	cin >> n;
	for (int i= 0; i < n; i++) {
		cin >> str;
		dic.push_back(str);
	}
	sort(dic.begin(), dic.end(), sortWord);
	dic.erase(unique(dic.begin(), dic.end()), dic.end());
	for (int i = 0; i < dic.size(); i++)
		cout << dic[i] << endl;
	return 0;
}