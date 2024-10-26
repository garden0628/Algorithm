#include <iostream>
#include <vector>
using namespace std;

#define ll long long

void solve() 
{
    ll n;
    cin >> n;

    ll s = n*(n+1)/2;
    vector<ll> v1, v2;
    ll s1=0;

    if (s%2==0) {
        cout << "YES" << endl;
        for (int i=n; i>0; --i) {
            if (s1+i <= s/2) {
                v1.push_back(i);
                s1 += i;
            } else {
                v2.push_back(i);
            }
        }

        cout << v1.size() << endl;
        for (int i=0; i<v1.size(); ++i) {
            cout << v1[i] << " ";
        }
        cout << endl;

        cout << v2.size() << endl;
        for (int i=0; i<v2.size(); ++i) {
            cout << v2[i] << " ";
        }
    } else {
        cout << "NO";
    }
}

int main() {
    solve();

    return 0;
}