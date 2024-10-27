#include <iostream>
using namespace std;

#define ll long long

void solve() {
    string str;
    cin >> str;

    int arr[26] = {0, };
    string ans = "";

    for (int i=0; i<str.size(); ++i) {
        arr[str[i]-'A'] += 1;
    }

    int pos = 0;
    for (int i=0; i<26; ++i) {
        if (arr[i]%2 == 1) pos += 1;
    }
    if (pos > 1) {
        cout << "NO SOLUTION";
    } else {
        for (int i=0; i<26; ++i) {
            if ((arr[i]%2) != 1) {
                for (int j=0; j<arr[i]/2; ++j) {
                    ans += char(i+'A');
                }
            }
        }

        for (int i=0; i<26; ++i) {
            if ((arr[i]%2) == 1) {
                for (int j=0; j<arr[i]; ++j) {
                    ans += char(i+'A');
                }
            }
        }

        for (int i=25; i>=0; --i) {
            if ((arr[i]%2) != 1) {
                for (int j=0; j<arr[i]/2; ++j) {
                    ans += char(i+'A');
                }
            }
        }
    }
    cout << ans;
}


int main() {
	solve();

	return 0;
}
