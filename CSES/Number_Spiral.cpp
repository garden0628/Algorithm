#include <iostream>
using namespace std;

#define ll long long

void solve() 
{
    ll t;
    cin >> t;

    for (int i=0; i<t; ++i) {
        ll y, x;
        cin >> y >> x;

        ll z = max(x, y);
        ll mx = z*z - (z-1);

        ll answer;
        if (z == y) {
            if (z%2==0){
                answer = mx + (z-x);
            } else {
                answer = mx - (z-x);
            }
        } else {
            if (z%2==0) {
                answer = mx - (z-y);
            } else {
                answer = mx + (z-y);
            }
        }
        cout << answer << endl;
    }
}

int main() {
    solve();

    return 0;
}