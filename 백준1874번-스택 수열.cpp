#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int ans[n]={0, };
    for(int i=0; i<n; i++){
        cin >> ans[i];
    }

    stack<int> start;
    for(int i=n; i>=1; i--){
        start.push(i);
    }

    stack<int> keep;
    vector<char> answer;
    int last;
    int index;
    for(index=0; index<n; index++){
        if(keep.size() == 0){
            while(1){
                if(ans[index] != start.top()){
                    keep.push(start.top());
                    start.pop();
                    answer.push_back('+');
                }
                else{
                    keep.push(start.top());
                    start.pop();
                    answer.push_back('+');
                    break;
                }
            }
            last = keep.top();
            keep.pop();
            answer.push_back('-');
        }
        else if(ans[index]<last){
            if(ans[index] != keep.top()){
                printf("NO");
                break;
            }
            else{
                last = keep.top();
                keep.pop();
                answer.push_back('-');
            }
        }
        else{
            while(1){
                if(ans[index] != start.top()){
                    keep.push(start.top());
                    start.pop();
                    answer.push_back('+');
                }
                else{
                    keep.push(start.top());
                    start.pop();
                    answer.push_back('+');
                    break;
                }
            }
            last = keep.top();
            keep.pop();
            answer.push_back('-');
        }
    }

    if(index == n){
        for(int i=0; i<answer.size(); i++){
            cout<<answer[i]<<" ";
        }
    }

    return 0;
}
