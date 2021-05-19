#include <iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int card[N];
    int arr[2][(N/2)+1];
    arr[0][0] = 0;
    arr[1][0] = 0;
    for(int i=0; i<N; i++){
        cin>>card[i];
        if(i%2==0){
            arr[0][(i/2)+1] = arr[0][i/2] + card[i];
        }
        else{
            arr[1][(i/2)+1] = arr[1][i/2] + card[i];
        }
    }

    int sum[N] = {0, };
    for(int i=0; i<N; i++){
        if(i%2==0){
            sum[i] = arr[0][i/2] + (arr[1][(N/2)] - arr[1][i/2]);
        }
        else{
            sum[i] = arr[0][(i/2)+1] + (arr[1][(N/2)] - arr[1][i/2] - card[N-1]);
        }
    }

    int max = 0;
    for(int i=0; i<N; i++){
        if(sum[i] > max){
            max = sum[i];
        }
    }
    cout<<max;

    return 0;
}
