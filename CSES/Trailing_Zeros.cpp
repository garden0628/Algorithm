#include <iostream>
using namespace std;

#define ll long long

void solve() {
	ll n;
	cin >> n;
	
	ll five=0;
    if (n<5) {
        cout << 0;
    } else {
        for (ll i=5; i<=n; i+=5) {
            ll nn = i;
            while (nn%5 == 0) {
                five += 1;
                nn /= 5;
            }
        }
        
        cout << five;
    }
}


int main() {
	solve();

	return 0;
}
