#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    int n;
	cin >> n;

    for (int i=0; i<n; ++i) {
        ll k;
        cin >> k;

        ll l=1, m=9;
        while (k>l*m) {
            k -= (l*m);
            l += 1;
            m *= 10;
        }

        ll idx = k/l;
        ll remain = k%l;

        ll start = pow(10, l-1);
        start += (idx-1);

        string ans;
        if (remain == 0) {
            ans = to_string(start);
            cout << ans[ans.size()-1] << endl;
        } else {
            ans = to_string(start+1);
            cout << ans[remain-1] << endl;
        }
    }
}


int main() {
	solve();

	return 0;
}
