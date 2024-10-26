#include <iostream>
using namespace std;

#define ll long long

void solve() 
{
    ll n;
    cin >> n;

    for (int i=1; i<=n; ++i) {
        ll k = i*i;
        ll pos = k*(k-1)/2;
        ll impos = 4*(i-1)*(i-2);
        ll ans = pos - impos;
        cout << ans << endl;
    }
}

int main() {
    solve();

    return 0;
}