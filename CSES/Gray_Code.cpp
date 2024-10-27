#include <iostream>
#include <queue>
using namespace std;

#define ll long long

void solve() {
    ll n;
    cin >> n;

    queue<string> q;
    q.push("0");
    q.push("1");

    for(int i=1; i<n; ++i) {
        int qsize = q.size();
        for (int j=0; j<qsize; ++j) {
            string temp = q.front();
            q.pop();
            if (j%2 ==0 ) {
                q.push(temp+"0");
                q.push(temp+"1");
            } else {
                q.push(temp+"1");
                q.push(temp+"0");
            }
            
        }
    }

    while(!q.empty()) {
        cout << q.front() << endl;
        q.pop();
    }
}

int main() {
    solve();
    return 0;
}