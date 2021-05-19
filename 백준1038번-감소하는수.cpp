#include<iostream>
#include<queue>
using namespace std;

int main(){
    int n;
    cin>>n;
    int count=0;

	if(n <= 10){
		cout<<n<<endl;
	}
	else if(n == 1022){
        cout<<9876543210<<endl;
	}
	else if(n >= 1023){
        cout<<"-1"<<endl;
	}
	else{
        int last_num, num;
        queue<int> decrease;
		for(int i=1; i<10; i++){
			decrease.push(i);
			count++;
		}
		while(count < n){
			num = decrease.front();
			decrease.pop();
			last_num = num%10;
			for(int j=0; j<last_num; j++){
				decrease.push(num*10 + j);
				count++;
				if(count == n){
					cout<<num*10 + j<<endl;
					break;
				}
			}
		}
	}
	return 0;
}
