#include <bits/stdc++.h>
using namespace std;

#define ll long long
static vector<ll> nums;
static int n;

ll recur(int idx, ll sum1, ll sum2) {
    if (idx == n) {
        return abs(sum1 - sum2);
    }

    ll left = recur(idx+1, sum1+nums[idx], sum2);
    ll right = recur(idx+1, sum1, sum2+nums[idx]);

    return min(left, right);
}

void solve() {
    cin >> n;

    for (int i=0; i<n; ++i) {
        ll n;
        cin >> n;
        nums.push_back(n);
    }

    ll ans = recur(0, 0, 0);
    cout << ans;
}

int main() {
    solve();
    return 0;
}
