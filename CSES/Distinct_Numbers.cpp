#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    ll n;
    cin >> n;

    vector<ll> v;
    for (int i=0; i<n; ++i) {
        ll x;
        cin >> x;
        v.push_back(x);
    }

    ll check = -1;
    int ans = 0;

    sort(v.begin(), v.end());
    for (int i=0; i<v.size(); ++i) {
        if (v[i] != check) {
            check = v[i];
            ++ans;
        }
    }

    cout << ans;
}

int main() {
    solve();
    return 0;
}