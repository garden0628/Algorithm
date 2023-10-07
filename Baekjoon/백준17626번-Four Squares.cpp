#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int num;
    cin >> num;

    int dp[50001];
    dp[0] = 0;
    dp[1] = 1;

    if(num==1){
        cout<<dp[1];
    }
    else{
        for(int i=2; i<=num; i++){
            dp[i] = 4;
            for(int j=1; j<=int(pow(i, 0.5)); j++){
                if(dp[i-(j*j)]<dp[i]){
                    dp[i] = dp[i-(j*j)]+1;
                }
            }
        }
        cout<<dp[num];
    }

    return 0;
}
