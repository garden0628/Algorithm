#include <iostream>
using namespace std;

#define ll long long

void solve() {
	ll n;
	cin >> n;
	
	ll ans = 1;
	for (int i=0; i<n; ++i) {
		ans = ans * 2 % ((int)1e9+7);
	}
	cout << ans;
}


int main() {
	solve();

	return 0;
}
