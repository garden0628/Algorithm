#include <iostream>

using namespace std;

int main()
{
    int N, L;
    cin>>N>>L;

    int sum;
    int divide=0;
    for(int i=L; i<=100; i++){
        sum = i*(i-1)/2;

        if((N-sum)%i==0 && (N-sum)/i>=0){
            divide = i;
            break;
        }

    }

    if(divide == 0){
        cout<<-1;
    }
    else{
        int plus = (N-sum)/divide;
        for(int i=0; i<divide; i++){
            cout<<i+plus<<" ";
        }
    }

    return 0;
}
