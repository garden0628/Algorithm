#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    string n;
	cin >> n;

    sort(n.begin(), n.end());

	set<string> ans;
    do {
        ans.insert(n);
    } while (next_permutation(n.begin(), n.end()));

    cout << ans.size() << endl;

    set<string>::iterator it;
    for (it=ans.begin(); it!=ans.end(); ++it) {
        cout << *it << endl;
    }
}


int main() {
	solve();

	return 0;
}
