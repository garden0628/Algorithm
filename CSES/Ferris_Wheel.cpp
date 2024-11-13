#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    ll n, x;
    cin >> n >> x;

    vector<ll> w;
    for (int i=0; i<n; ++i) {
        ll p;
        cin >> p;
        w.push_back(p);
    }

    sort(w.begin(), w.end());

    ll s = 0, e = w.size()-1;
    int ans = 0;

    while(s <= e) {
        if (s == e) {
            ++ans;
            break;
        }

        if (w[s] + w[e] <= x) {
            ++ans;
            ++s;
            --e;
        } else {
            ++ans;
            --e;
        }
    }

    cout << ans;
}

int main() {
    solve();
    return 0;
}