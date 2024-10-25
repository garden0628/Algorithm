#include <iostream>
using namespace std;

#define ll long long

void solve() 
{
    ll n, sum=0;
    cin >> n;

    for (int i=1; i<n; ++i) {
        int num;
        cin >> num;
        sum += num;
    }

    cout << n*(n+1)/2 - sum;
}

int main() {
    solve();

    return 0;
}