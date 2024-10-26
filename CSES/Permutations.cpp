#include <iostream>
using namespace std;

#define ll long long

void solve() 
{
    ll n;
    cin >> n;

    if (n==1) {
        cout << n;
    } else if (n== 2 || n==3) {
        cout << "NO SOLUTION";
    } else {
        int i;
        if (n%2 == 1) {
            for (i=1; i<=n; i+=2) cout << i << " ";
            for (i=2; i<=n; i+=2) cout << i << " ";
        } else {
            for (i=2; i<=n; i+=2) cout << i << " ";
            for (i=1; i<=n; i+=2) cout << i << " ";
        }
    }
}

int main() {
    solve();

    return 0;
}