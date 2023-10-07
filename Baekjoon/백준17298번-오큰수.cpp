#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    stack<int> seq;
    stack<int> keep;
    stack<int> ans;

    int count;
    cin >> count;

    int num;
    for(int i=0; i<count; i++){
        cin >> num;
        seq.push(num);
    }

    ans.push(-1);
    keep.push(seq.top());
    seq.pop();

    for(int i=0; i<count-1; i++){
        while(1){
            if(seq.top()<keep.top()){
                ans.push(keep.top());
                keep.push(seq.top());
                seq.pop();
                break;
            }
            else{
                keep.pop();
                if(keep.size() == 0){
                    ans.push(-1);
                    keep.push(seq.top());
                    seq.pop();
                    break;
                }
            }
        }
    }

    for(int i=0; i<count; i++){
        cout<<ans.top()<<" ";
        ans.pop();
    }
    return 0;
}
