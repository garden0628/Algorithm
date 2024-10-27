#include <iostream>
using namespace std;

#define ll long long

void solve() {
	ll t;
	cin >> t;
	
    for (ll i=0; i<t; ++i) {
        ll a, b;
        cin >> a >> b;

        if ((a+b)%3==0 && 2*a>=b && 2*b>=a) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}


int main() {
	solve();

	return 0;
}
