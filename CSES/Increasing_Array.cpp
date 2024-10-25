#include <iostream>
using namespace std;

#define ll long long

void solve() 
{
    ll n, answer=0;
    cin >> n;

    ll mx=0;
    for (int i=0; i<n; ++i) {
        ll x;
        cin >> x;

        mx = max(mx, x);
        answer += mx-x;
    }

    cout << answer;
}

int main() {
    solve();

    return 0;
}