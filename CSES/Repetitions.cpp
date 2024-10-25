#include <iostream>
#include <string>
using namespace std;

#define ll long long

void solve() 
{
    ll cnt=1, answer=0;
    string str;

    cin >> str;
    for(int i=0; i<str.length()-1; ++i) {
        if (str[i] == str[i+1]) {
            cnt += 1;
        } else {
            if (cnt > answer) answer = cnt;
            cnt = 1;
        }
    }
    if (cnt > answer) answer = cnt;

    cout << answer;
}

int main() {
    solve();

    return 0;
}