#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    ll n, m, k;
    cin >> n >> m >> k;

    vector<ll> applies, aparts;
    for (int i=0; i<n; ++i) {
        ll a;
        cin >> a;
        applies.push_back(a);
    }

    for (int i=0; i<m; ++i) {
        ll a;
        cin >> a;
        aparts.push_back(a);
    }

    sort(applies.begin(), applies.end());
    sort(aparts.begin(), aparts.end());

    ll applies_idx=0, aparts_idx=0, ans=0;
    while (applies_idx<applies.size() && aparts_idx<aparts.size()) {
        if (aparts[aparts_idx] < applies[applies_idx] - k) {
            aparts_idx++;
        } else if ((applies[applies_idx]-k <= aparts[aparts_idx]) && (aparts[aparts_idx] <= applies[applies_idx]+k)) {
            ans++;
            aparts_idx++;
            applies_idx++;
        } else {
            applies_idx++;
        }
    }

    cout << ans;
}

int main() {
    solve();
    return 0;
}